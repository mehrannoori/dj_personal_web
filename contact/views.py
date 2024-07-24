from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Message

class MessagesList(PermissionRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'contact/list_message.html'
    permission_required = 'contact.list_message_permit'

class MessageCreate(CreateView):
    model = Message
    fields = ['name', 'email', 'message']
    success_url = reverse_lazy('home')
    template_name = 'contact/send_message.html'

class MessageDeleteView(PermissionRequiredMixin, DeleteView):
    model = Message
    context_object_name = 'message'
    template_name = 'contact/delete_message.html'
    success_url = reverse_lazy('list_message')
    permission_required = 'contact.list_messsage_permit'