from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Testimonial
from .serializers import TestimonialSerializer

# Create your views here.

class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    permission_classes = [AllowAny]