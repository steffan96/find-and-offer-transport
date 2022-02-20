from django.core.management.base import BaseCommand, CommandError
from ...models import Post
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Soft-deleting objects older than 40 days'

    def handle(self, *args, **kwargs):
        a = Post.objects.filter(
            created__lte=datetime.now()-timedelta(days=40)).all()
        self.stdout.write('Soft-deleted objects older than 40 days')
        for i in a.iterator():
            i.soft_delete()
            