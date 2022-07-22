from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.models import Message

from app.serializers import MessageSerializer


# class MessageAPIView(APIView):

    # permission_classes = [AllowAny,]
    # http_method_names = ['post',]
    # serializer_class = MessageSerializer
    # def post(self, request, format=None):
    #     serializer = MessageSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AllowAny,)

    @action(methods=['post'], detail=False, serializer_class=MessageSerializer)
    def user_register(self, request):
        serialized_data = MessageSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        data = {'message': 'Message successfully sended !'}
        return Response(data, status.HTTP_201_CREATED)
