from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCrearteView, BlogEditView, BlogDeleteView, SearchResultsView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCrearteView.as_view(), name='add_post'),
    path('post/<int:pk>/edit', BlogEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('search/', SearchResultsView.as_view(), name='search_post'),
]