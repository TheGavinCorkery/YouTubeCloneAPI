from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('replies/', views.ReplyList.as_view()),
    path('comment/reply/<int:comment_id>', views.ReplyList.as_view()),

]