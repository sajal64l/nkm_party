from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import *
from .forms import *
from notice.models import Post

# Create your views here.
def index(request):
    gallery = Gallery.objects.all()
    posts = Post.objects.all()[:3]
    speech = Speech.objects.all()[:4]
    history = History.objects.all()[:3]
    faq = FAQ.objects.all()[:3]
    context = {
        'gallery':gallery,
        'posts':posts,
        'speech':speech,
        'history' :history,
        'faq':faq,
    }
    return render(request, 'frontend/index.html', context)

def about(request):
    return render(request, 'frontend/about.html')

def history(request):
    history = History.objects.all()
    context = {
        'history':history,
    }
    return render(request, 'frontend/history.html', context)

def donation(request):
    return render(request, 'frontend/donation.html')

def member(request):
    if request.method == 'POST':
        member_form = MemberForm(data=request.POST)
        if member_form.is_valid():
            member_form.save()
            messages.success(request, "Member Request Successfully Submitted")
        else:
            messages.error(request, "Please fill all the required fields correctly")
    else:
        member_form = MemberForm() 
    context = {
        'member_form':member_form,
    }
    return render(request, 'frontend/member.html', context)

def contact(request):
    return render(request, 'frontend/contact.html')

