from django.shortcuts import render

from .forms import UrlForm


# Create your views here.
def shortcut_view(request):
    form = UrlForm()
    return render(request, 'base.html', {'form': form})
