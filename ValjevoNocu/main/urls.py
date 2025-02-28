from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns =[
    path("",views.home,name="home"),
    path("relja/",views.relja,name="relja"),
    path('dogadjaj/',views.create_svirka,name='create_svirka'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)