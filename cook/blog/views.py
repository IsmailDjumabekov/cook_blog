from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DataMixin

from blog.models import Post

class HomeView(DataMixin, ListView):
    model = Post
    paginate_by = 9
    template_name = "blog/home.html"

    def get(self, request, *args, **kwargs):
        self.get_data()
        return super().get(request, *args, **kwargs)

    def get_data(self):
        self.extra_context = {
            'title': 'Blog sheff',
            'tagline': 'Blog about recipe',
        }


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'



