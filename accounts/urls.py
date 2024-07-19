from django.urls import path

from .views import SignupPageView, AccountListView, AccountEditView, AccountDeleteView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('users/', AccountListView.as_view(), name='users'),
    path('edit/<int:pk>/', AccountEditView.as_view(), name='edit_user'),
    path('delete/<int:pk>/', AccountDeleteView.as_view(), name='delete_user'),
]