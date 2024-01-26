from django.shortcuts import render,redirect
from . import forms, models
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            messages.success(request, 'Album added successfully')
            return redirect('home')
    else:
        album_form = forms.AlbumForm()
        
    return render(request, 'album.html', {'form' : album_form, 'type':'Add Album'})

@login_required
def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            messages.success(request, 'Album updated successfully')
            return redirect('home')
        
    return render(request, 'album.html', {'form' : album_form, 'type':'Edit Album'})

@login_required
def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    messages.success(request, 'Album deleted successfully')
    return redirect('home')