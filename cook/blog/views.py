from django.views.generic import ListView, DetailView,CreateView
from django.views.generic.edit import DataMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.views import APIView

from .models import Post, Comment, Category
from .forms import CommentForm
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PostSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     # queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#
#         if not pk:
#             return Post.objects.all()[:3]
#         return Post.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )

class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly, )

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()

        return context

class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()



