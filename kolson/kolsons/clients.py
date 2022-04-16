from django.db import models

# creating model for clients database
class clientsM(models.Model):
    # id = models.IntegerField(primary_key=True)
    logo = models.ImageField(upload_to='clients/logos')
    companyName = models.CharField(max_length=200)