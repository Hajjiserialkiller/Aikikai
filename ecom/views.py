from django.http import HttpResponse
from django.shortcuts import render
from .models import Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request, 'ecom/index.html')

def video_list(request):
    video_list = Video.objects.order_by('-video_uploaded_at')
    paginator = Paginator(video_list, 9)  # 3 videos per page

    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    return render(request, 'ecom/videos.html', {'videos': videos})

def onset(request):
    return render(request, 'ecom/onset.html')