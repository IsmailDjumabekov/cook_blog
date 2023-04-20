from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', cache_page(60*10)(views.PostListView.as_view()), name="post_list"),
    path('', cache_page(60*10)(views.HomeView.as_view()), name="home"),
]

