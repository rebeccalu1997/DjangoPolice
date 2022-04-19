from django.shortcuts import render
from .models import post
# Create your views here.
def Home(request):
    posts = post.objects.all()
    context= {'posts': posts}
    return render(request, 'PoliceProject/home.html' , context)