from django.core.paginator import Paginator, EmptyPage
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
