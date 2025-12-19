from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TestimonialViewSet, CertificateViewSet
from django.urls import path
from . import views
from Content.views import healthz

router = DefaultRouter()
router.register(r"testimonials", TestimonialViewSet, basename="testimonial")
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"certificates", CertificateViewSet, basename="certificate")

urlpatterns = router.urls + [path("healthz/", healthz, name="healthz")]