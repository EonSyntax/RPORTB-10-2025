import os
from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Content'

    def ready(self):
        if os.environ.get("CREATE_SUPERUSER", "false").lower() == "true":
            from .utils import create_admin_user

            def create_user_after_migrate(sender, **kwargs):
                try:
                    create_admin_user()
                except Exception as e:
                    print(f"⚠ Superuser creation failed: {e}")

            post_migrate.connect(create_user_after_migrate, weak=False)