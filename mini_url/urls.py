from django.urls import path

from .views import shortcut_view

urlpatterns = [
    path('', shortcut_view, name='shortcut'),
]
