from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = ["id", "name", "designation", "quote", "image_url"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
