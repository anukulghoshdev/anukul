from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from user_auth.forms import SignUpForm, UserProfileChangeForm, UserProfilePic


# Create your views here.
def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {
        'form': form,
        'registered' : registered
    }
    return render(request, 'user_auth/sign_up.html', context=dict)


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app1:home'))
    dict = {
        'form':form,
    }
    return render(request, 'user_auth/login.html', context=dict)


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_auth:log_in'))


@login_required
def profile(request):
    return render(request, 'user_auth/profile.html', context={})


@login_required
def user_profile_change(request):
    current_user = request.user
    form = UserProfileChangeForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChangeForm(instance=current_user)
            return HttpResponseRedirect(reverse('user_auth:profile'))
    return render(request, 'user_auth/user_profile_change.html', context={'form':form})


@login_required
def password_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    password_changed = False

    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            password_changed = True
    return render(request, 'user_auth/password_change.html', context={'form':form, 'password_changed':password_changed })


@login_required
def add_pro_pic(request):
    form = UserProfilePic()
    if request.method == 'POST':
        form = UserProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('user_auth:profile'))
    return render(request, 'user_auth/add_pro_pic.html', context={'form':form})


@login_required
def change_pro_pic(request):
    form = UserProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = UserProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_auth:profile'))
    return render(request, 'user_auth/add_pro_pic.html', context={'form':form})
