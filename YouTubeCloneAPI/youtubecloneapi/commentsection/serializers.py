from rest_framework import serializers
from .models import Replies
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'messages', 'likes', 'dislikes']

class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ['id', 'message']