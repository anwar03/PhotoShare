from django.shortcuts import render, redirect
from .forms import AlbumForm

def AlbumUpload(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'album.html', {
        'form': form
    })
