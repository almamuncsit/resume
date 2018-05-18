from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    data = {}
    data['about'] = About.objects.all()[0]
    data['social'] = Social.objects.all()[0]
    data['experiences'] = Experience.objects.order_by("-id").all()
    data['educations'] = Education.objects.order_by("-id").all()
    data['skillCategories'] = SkillCategory.objects.order_by("order").all()
    return render(request, 'index.html', data)

