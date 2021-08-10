from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Мозг самого сайта


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class ConfirmCode(models.Model):
    code = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_until = models.DateTimeField(null=True)

    def __str__(self):
        return self.code
