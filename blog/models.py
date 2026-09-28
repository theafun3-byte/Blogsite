from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PD', 'Published'
    title = models.CharField(max_lenght=250)
    slug = models.SlugField(max_lenght=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_lenght=2,
                                choices=Status.choices,
                                default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes =[
            models.Index(fields=['-publish'])
            ]

    def _str_(self):
        return self.title
