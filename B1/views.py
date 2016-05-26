from django.shortcuts import render
import populate
from models import Analytics

def index(request):
    entries = Analytics.objects.all()
    return render(request, 'B1/index.html', {'Analytics': entries})
