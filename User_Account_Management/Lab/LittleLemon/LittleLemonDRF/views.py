from django.shortcuts import render
from rest_framework import generics
from .serializers import RatingSerializer
from .models import Rating
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class RatingView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if(self.request.method == 'GET'):
            return []
        
        return [IsAuthenticated()]