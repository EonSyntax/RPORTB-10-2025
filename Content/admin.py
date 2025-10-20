from django.contrib import admin
from .models import Testimonial

# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "designation", "quote")

