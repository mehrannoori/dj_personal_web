from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from .models import Post

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class BlogCrearteView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'body', 'cover']
    login_url = 'login'
    permission_required = 'blog.special_status'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body', 'cover']
    login_url = 'login'
    permission_required = 'blog.special_status'


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog')
    login_url = 'login'
    permission_required = 'blog.special_status'

class SearchResultsView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query == '':
            return Post.objects.filter(title__icontains='123456789')
        else:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )