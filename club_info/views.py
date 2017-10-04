from django.shortcuts import render
from .models import *

# Create your views here.
def getClubList(request):
    clublist = ClubInfo.objects.all()
    return render(request, 'club/base.html', {'clist':clublist})
