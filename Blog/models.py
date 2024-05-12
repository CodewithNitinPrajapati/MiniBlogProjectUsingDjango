from django.db import models

class Post(models.Model):
    title = models.CharField( max_length=50)
    desc = models.TextField()


class ContactModel(models.Model):
    first_name =models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
