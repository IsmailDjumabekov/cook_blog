from django.views.generic import ListView, DetailView,CreateView
from django.views.generic.edit import DataMixin
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Post, Comment
from .forms import CommentForm
from .serializers import PostSerializer


class BlogAPIView(APIView):
    def get(self, request):
        lst = Post.objects.all()
        return Response({'posts': PostSerializer(lst, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post', serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put not allowed"})

        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Object is not exists"})

        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE now allowed"})

        try:
            article = Post.objects.get(pk=pk)
            article.delete()
        except:
            return Response({"error": "Object does not exists"})
        return Response({"post": "delete post " + str(pk)})



# class BlogAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = BlogSerializer

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



