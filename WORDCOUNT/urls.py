
from django.contrib import admin
from django.urls import path
import count.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',count.views.home,name='home'),
    path('about/',count.views.about,name='about'),
    path('result/',count.views.result,name='result'),
]