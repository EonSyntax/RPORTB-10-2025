from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    quote = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.designation}"