from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(blank=True, verbose_name="Article text")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time creating")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time editing")
    is_published = models.BooleanField(default=True, verbose_name="Published")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name