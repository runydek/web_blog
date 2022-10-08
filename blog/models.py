from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='blogs')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-")
        return super().save(*args, **kwargs)

