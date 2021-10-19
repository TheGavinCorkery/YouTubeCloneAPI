from django.urls import path
from . import views

urlpatterns = [
    # Get all comments by video and used to post
    path('comments/<str:video>/', views.CommentList.as_view()),
    # Get single comment by comment ID
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    # Get all replies and used to post
    path('replies/<int:comment>', views.ReplyList.as_view()),
    # Get single reply by reply ID
    path('comment/<int:pk>/reply', views.ReplyDetail.as_view()),
    # Like/Dislike Comment
    path('comments/<int:pk>/thumbs_up', views.CommentLikes.as_view()),
    path('comments/<int:pk>/thumbs_down', views.CommentLikes.as_view()),
    # Post reply to comment by ID
    path('comments/reply/<int:comment>', views.ReplyList.as_view()),
    # Get all replies by video
    path('commentsection/<str:video>/', views.CommentSection.as_view()),
]