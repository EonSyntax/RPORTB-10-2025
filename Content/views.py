from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Project, Testimonial
from .serializers import ProjectSerializer, TestimonialSerializer
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def healthz(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        # database is up
        return HttpResponse("OK", status=200)
    except Exception:
        return HttpResponse("DB Error", status=500)

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