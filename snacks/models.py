from django.db import models
from django.contrib.auth import get_user_model  # added
from django.urls import reverse  # added

# Create your models here.


class Snack(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detailView", args=[str(self.id)])


# reverse("detailView", args=[str(self.id)])
