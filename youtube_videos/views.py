from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response

from youtube_videos.models import Video


@api_view(('GET',))
def get_page(request, page_number):
    video_list = Video.objects.all().order_by('-published_date')
    paginator = Paginator(video_list, 20)
    page_obj = paginator.get_page(page_number)
    return Response({"data": page_obj})
