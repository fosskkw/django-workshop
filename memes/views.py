from django.shortcuts import render
from .models import Meme

def meme_list(request):
    memes = Meme.objects.all()
    return render(request, 'memes/meme_list.html', {'memes': memes})