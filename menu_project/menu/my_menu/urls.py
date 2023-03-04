from django.urls import path
from my_menu.views import index
urlpatterns = [
    path('',index)
]