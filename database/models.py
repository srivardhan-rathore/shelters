from django.db import models


class Division(models.Model):
    division = models.CharField(max_length=10)

    def __str__(self):
        return self.division


class Category(models.Model):
    category = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class College(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, default="Bengaluru")
    state = models.CharField(max_length=100, default="Karnataka")

    def __str__(self):
        return self.name


class PayingGuest(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, default="Bengaluru")
    state = models.CharField(max_length=100, default="Karnataka")
    college = models.ManyToManyField(College)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

