from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.JSONField(default=list)  # stores an array of strings
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default'
    )

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return ""





class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    quote = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.designation}"



class Certificate(models.Model):
    organization_name = models.CharField(max_length=200)
    certificate_name = models.CharField(max_length=200)
    certificate_id = models.CharField(max_length=200, blank=True, null=True)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    verify_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.certificate_name} — {self.organization_name}"

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return ""