from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="root").exists():
            User.objects.create_superuser("root", "root@admin.com", "R@ni43210")