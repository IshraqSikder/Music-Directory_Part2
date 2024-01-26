from django.shortcuts import render,redirect
from . import forms, models
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
            
    return render(request, 'musician.html', {'form': register_form, 'type':'Register'})

class UserLoginView(LoginView):
    template_name = 'musician.html'
    def get_success_url(self):
        return reverse_lazy('edit_profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in informations are incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@login_required  
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            messages.success(request, 'Musician added successfully')
            return redirect('home')
    else:
        musician_form = forms.MusicianForm()
        
    return render(request, 'musician.html', {'form' : musician_form, 'type':'Add Musician'})

@login_required   
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('edit_profile')
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
            
    return render(request, 'musician.html', {'form': profile_form, 'type':'Edit Profile'})

@login_required
def user_logout(request):
    messages.success(request, 'Logged out successfully')
    logout(request)
    return redirect('login')

def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)
    
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            messages.success(request, 'Musician updated successfully')
            return redirect('home')
        
    return render(request, 'musician.html', {'form' : musician_form, 'type':'Edit Musician'})