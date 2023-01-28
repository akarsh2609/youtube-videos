from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from youtube_videos.models import Video
from youtube_videos.serializers import VideoSerializer


@api_view(('GET',))
def get_page(request, page_number):
    video_list = Video.objects.all().order_by('-published_date')
    paginator = Paginator(video_list, 20)
    try:
        video_list = paginator.page(page_number)
    except EmptyPage:
        # return last page
        video_list = paginator.page(paginator.num_pages)
    return Response(data=VideoSerializer(video_list, many=True).data, status=200)


@api_view(('GET',))
def search_video(request):
    filter_string = request.GET.get('filter_string', '')
    filter_string_regex = filter_string.replace(' ', '|')
    video_list = Video.objects.all().filter(
        Q(title__iregex=filter_string_regex) | Q(description__iregex=filter_string_regex))[:50]
    return Response(data=VideoSerializer(video_list, many=True).data, status=200)
