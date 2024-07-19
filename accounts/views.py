from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class AccountListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'accounts'
    template_name = 'registration/account_list.html'
    login_url = 'login'
    permission_required = 'accounts.account_permissions'

class AccountEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'registration/account_edit.html'
    fields = ['email', 'username', 'first_name', 'last_name']
    success_url = reverse_lazy('users')
    login_url = 'login'
    permission_required = 'accounts.account_permissions'

class AccountDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'registration/account_delete.html'
    success_url = reverse_lazy('users')
    login_url = 'login'
    permission_required = 'accounts.account_permissions'