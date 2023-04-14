from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('contact/', cache_page(60*10)(views.ContactView.as_view()), name="contact"),
    path('about/', cache_page(60*10)(views.AboutView.as_view()), name="about"),
    path('feedback/', views.CreateContact.as_view(), name="feedback"),
]