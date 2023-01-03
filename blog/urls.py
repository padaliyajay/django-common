from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blog_home'),
    path('category/<slug:slug>', views.CategoryView.as_view(), name='blog_category'),
    path('search', views.SearchView.as_view(), name='blog_search'),
    path('post/<slug:slug>', views.PostView.as_view(), name='post'),
    path('comment_form/<slug:slug>', views.CommentCreateView.as_view(), name='blog_comment_form'),
]