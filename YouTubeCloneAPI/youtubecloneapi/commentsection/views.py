from django.shortcuts import render
from django.http.response import Http404
from .models import Comments
from .models import Replies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from .serializers import RepliesSerializer

# Create your views here.

# Comment views
class CommentList(APIView):
    def get(self, request):
        comment = Comments.objects.all()
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer._errors, status = status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk = pk)
        except Comments.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


# Replies Views
class ReplyList(APIView):
    def get(self, request):
        reply = Replies.objects.all()
        serializer = RepliesSerializer(reply, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RepliesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer._errors, status = status.HTTP_400_BAD_REQUEST)

class ReplyDetail(APIView):

    def get_object(self, pk):
        try:
            return Replies.objects.get(pk = pk)
        except Replies.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reply = self.get_object(pk)
        serializer = RepliesSerializer(reply)
        return Response(serializer.data)
