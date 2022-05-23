from django.shortcuts import render

from .models import StudentData
# Create your views here.

def home(request):
    students= StudentData.objects.all()
    context= {'students': students}
    return render(request, 'home.html', context)