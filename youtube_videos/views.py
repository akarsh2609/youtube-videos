from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response

from youtube_videos.models import Video
from youtube_videos.serializers import VideoSerializer


@api_view(('GET',))
def get_page(request, page_number):
    video_list = Video.objects.all().order_by('-published_date')
    paginator = Paginator(video_list, 20)
    videos = paginator.page(page_number)
    return Response(data=VideoSerializer(videos, many=True).data, status=200)
