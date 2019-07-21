from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'media'
urlpatterns = [
    path('', views.MediaEntryList.as_view(), name='media-list'),
    path('create/', views.MediaEntryCreate.as_view(), name='media-create'),
    path('update/<int:pk>/', views.MediaEntryUpdate.as_view(), name='media-update'),
    path('delete/<int:pk>/', views.MediaEntryDelete.as_view(), name='media-delete'),
    path('view/<int:pk>/', views.MediaEntryDetail.as_view(), name='media-detail'),
    path('user_posts/<int:pk>/', views.MyPosts.as_view(), name='user-posts'),
]
