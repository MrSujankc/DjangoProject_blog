from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from .forms import EditForm
#def home(request):
#   return render(request, 'theblog/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'
    context_object_name = 'posts'
    #ordering = ['-id']
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/add_post.html' 
    success_url = reverse_lazy('theblog:home') 
    #fields = '__all__'   
    #fields = ('title', 'content')


class UpdatePostView(UpdateView):
    model = Post
    form_class =EditForm
    template_name = 'theblog/update_post.html'
    success_url = reverse_lazy('theblog:home')
    #fields = ['title', 'title_tag', 'content']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'  
    success_url = reverse_lazy('theblog:home')  