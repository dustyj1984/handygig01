from django.views.generic import ListView, DetailView 
from django.views.generic.edit import ( 
    CreateView,
    UpdateView,
    DeleteView,

)

from django.urls import reverse_lazy

from .models import Post, Status, Comment
from .forms import CommentForm

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = Status.objects.get(id=1)
        context['posts_list'] = Post.objects.filter(
            status=status).order_by("created_on").reverse()
        return context

class DraftPostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    status = Status.objects.get(id=2)
    context["posts_list"] = Post.objects.filter(
        status=status).filter(author=self.request.user
        ).order_by("created_on").reverse()
    return context

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post   

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'subtitle', 'image', 'body', 'author', 'status']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(UpdateView):
    template_name = "posts/update.html"
    model = Post
    fields = ['title', 'subtitle', 'image', 'body', 'author', 'status']



    def test_func(self):
        post_obj = self.get_object()
        return self.request.user == post_obj.author

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy('list')

class PostCommentView(CreateView):
    template_name = "posts/comment.html"
    model = Comment
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(id=self.kwargs['pk'])
        context['post'] = post
        context["comments"] = Comment.objects.filter(post=post)
        return context

    def form_valid(self, form):
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})
   












# Create your views here.
