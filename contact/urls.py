from django.urls import path

from .views import MessagesList, MessageCreate, MessageDeleteView

urlpatterns = [
    path('', MessageCreate.as_view(), name='send_message'),
    path('list/', MessagesList.as_view(), name='list_message'),
    path('delete/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),
]