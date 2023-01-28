from django.views.generic import ListView, DetailView
from django.views.generic.edit import ( 
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post, Status

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        status = Status.objects.get(id=1)
        context["posts_list"] = Post.objects.filter(
            status=status).order_by("created_on").reverse()
        return context

class DraftPostListView(ListView):
    template_name = "posts/drafts.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(
            status=status).order_by('-created_on').reverse()
        return context

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post    

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'subtitle', 'body', 'author', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    template_name = "posts/update.html"
    model = Post
    fields = ['title', 'subtitle', 'body', 'author', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy('list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user




# Create your views here.
