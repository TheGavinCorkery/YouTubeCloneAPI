from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('replies/', views.ReplyList.as_view()),
    path('comment/<int:pk>/reply', views.ReplyDetail.as_view()),
    path('comment/<int:pk>/thumbs_up', views.CommentLikes.as_view()),
    path('comment/<int:pk>/thumbs_down', views.CommentLikes.as_view()),
]