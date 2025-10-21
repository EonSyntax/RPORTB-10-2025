from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Project, Testimonial
from .serializers import ProjectSerializer, TestimonialSerializer

# Create your views here.

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides only GET (list and retrieve) for projects.
    """
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer



class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    permission_classes = [AllowAny]