from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(blank=True)
    checked = models.CharField(max_length=5, blank=True, choices=(("Y", "Yes"), ("N", "No")))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    message = models.CharField(max_length=200)
    image = models.CharField(max_length=5000, null=True, blank=True)
    occupation = models.CharField(max_length=30, null=True, blank=True)


class Partners(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=5000, null=True, blank=True)


class ServiceInfo(models.Model):
    happy_clients = models.IntegerField()
    hard_worker = models.IntegerField()
    tie_ups = models.IntegerField()
    support = models.IntegerField()