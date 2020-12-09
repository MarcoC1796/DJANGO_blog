from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here. (no longer in use)
def home(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'blog/home.html', context)

# class based view (list type) associated with a model
# the diferece: we set the setting, not the logic
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # changes <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # uses 'posts' instead of object_list
    ordering = ('-date_posted',)

class PostDetailView(DetailView):
    model = Post

# 'LoginRequiredMixin' used instead of decorators to require login for class based views
class PostCreateView(LoginRequiredMixin,CreateView): # blog/post_form.html default route
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# 'UserPassesTestMixin' used to confirm that user is updating its posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # blog/post_form.html default route
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})