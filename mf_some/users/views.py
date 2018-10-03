from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from improved_user.forms import UserCreationForm

from .forms import UserUpdateForm
from .models import FriendRelationship

User = get_user_model()


class UserListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('friends')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('friends')


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/signup.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'

    def get_object(self):
        # only the user can edit the user
        return get_object_or_404(self.model, pk=self.request.user.pk)


class UserInviteView(LoginRequiredMixin, SingleObjectMixin, RedirectView):
    model = User
    url = reverse_lazy('users:list')

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        request.user.add_friend(user)
        return super().get(request, *args, **kwargs)


class UserAcceptInviteView(LoginRequiredMixin, SingleObjectMixin, RedirectView):
    model = FriendRelationship
    url = reverse_lazy('users:list')

    def get(self, request, *args, **kwargs):
        friend_relationship = self.get_object()
        friend_relationship.accept_invite()
        return super().get(request, *args, **kwargs)
