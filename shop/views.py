from django.shortcuts import render
from django.http import HttpResponse  # импорт для функции index(request)
# from . import models
from .models import Course
# Create your views here.


def index(request):
    courses = Course.objects.all()
    # return HttpResponse("Hello from the Shop app")
    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))
    # return HttpResponse(courses)
    return render(request, 'courses.html',{'courses':courses})
