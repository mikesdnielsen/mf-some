from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import PostCreateForm
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.select_related('author').annotate(likes_sum=Sum('likes'))


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostCreateForm

    def get_initial(self):
        return {'author': self.request.user.pk}

    def get_success_url(self):
        return reverse_lazy('posts:detail', args={'pk': self.object.pk})
