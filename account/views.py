from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Account, UserProfile

#ACCOUNT
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username = request.POST['username']
        email      = request.POST['email']
        password   = request.POST['password']
        
        user = Account.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
        profile = UserProfile.objects.create(user=user, profile_picture='')

        user.set_password(password)
        user.save()
        profile.save()

        return redirect('/account/login')
    else:
        pass

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            print('zzzzzzzzz')
            auth.login(request, user)
            return redirect('/onirix/form')

    return render(request, 'login.html')

def logout(request):
    try:
        auth.logout(request)
        return redirect('/account/login')
    except:
        pass


#USER_PROFILE
@login_required
def show_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    return render(request, 'show_profile.html', {'profile':profile})


    return render(request, 'index.html', {})

@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    # try:
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic', False)
        age = int(request.POST['age'])
        occupation = request.POST['occupation']

        profile.profile_picture = profile_pic
        profile.age = age
        profile.occupation = occupation
        profile.save()

    return render(request, 'edit_profile.html')

