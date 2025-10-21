from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TestimonialViewSet

router = DefaultRouter()
router.register(r"testimonials", TestimonialViewSet, basename="testimonial")
router.register(r"projects", ProjectViewSet, basename="project")

urlpatterns = router.urls