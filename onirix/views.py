from django.shortcuts import render, redirect
from .models import Dream
from account.models import UserProfile
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def dream_form(request):
    if request.method == 'POST':
        print(request.POST)
        user_profile = UserProfile.objects.get(user=request.user)
        dream_detail = request.POST['dream_detail']
        emotion_during_detail = request.POST['emotion_during_detail']
        emotion_waking_detail = request.POST['emotion_waking_detail']
        event_related_detail = request.POST['event_related_detail']
        dream_symbolize_detail = request.POST['dream_symbolize_detail']
        similar_dream_detail = request.POST['similar_dream_detail']

        dream = Dream.objects.create(user_profile=user_profile, dream_detail=dream_detail, emotion_during_detail=emotion_during_detail, emotion_waking_detail=emotion_waking_detail, 
                             event_related_detail=event_related_detail, dream_symbolize_detail=dream_symbolize_detail, similar_dream_detail=similar_dream_detail)
        dream.save()
        return redirect('loading')

    return render(request, 'dream_form.html')

@login_required(login_url='login')
def horoscope(request):

    return render(request, 'horoscope.html')

@login_required(login_url='login')
def about(request):

    return render(request, 'about.html')

@login_required(login_url='login')
def profile(request):
    
    return render(request, 'profile.html')

@login_required(login_url='login')
def loading(request):

    return render(request, 'loading.html')