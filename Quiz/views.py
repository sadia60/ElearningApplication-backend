from django.shortcuts import render
from .models import Mcq,Result
from .serializers import McqSeriailizer,ResultSeriailizer
from django.http import Http404

# Create your views here.
from rest_framework import generics


# Create your views here.s
class McqList(generics.ListCreateAPIView):
    queryset = Mcq.objects.all()
    serializer_class = McqSeriailizer


class ResultList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSeriailizer


