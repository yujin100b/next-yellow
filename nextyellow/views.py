from django.shortcuts import render
from .models import HitCount
from django.utils import timezone

# Create your views here.
def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    

    try:
        # ip주소와 게시글 번호로 기록을 조회함
        hits = HitCount.objects.get(ip=ip)
    except Exception as e:
        # 처음 게시글을 조회한 경우엔 조회 기록이 없음
        print(e)
        hits = HitCount.objects.create(ip=ip)
        hits.save()
    else:
        # 조회 기록은 있으나, 날짜가 다른 경우
        if not hits.date == timezone.now().date():
            hits = HitCount.objects.create(ip=ip)
        # 날짜가 같은 경우
        else:
            print(str(ip) + ' has already hit this post.\n\n')
  
    hitcount = hits.id 

    return render(request, 'nextyellow/index.html', { 'hitcount' : hitcount})