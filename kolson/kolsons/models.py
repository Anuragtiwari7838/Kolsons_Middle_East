from distutils.command.upload import upload
from django.db import models

# Create your models here. path("index/<int:id>",viewss.ind) , href="index/object.id"

class Product(models.Model):
    part_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=200,default="")
    images = models.ImageField(upload_to='document')
    Mounting_Style = models.CharField(max_length=200,blank=True,default="")
    Front_Protection = models.CharField(max_length=200,default="")
    Mounting_Cut_out = models.CharField(max_length=200,default="")
    Terminal = models.CharField(max_length=200,blank=True,default="")
    Front_Dimension = models.CharField(max_length=200,blank=True,default="")
    Operating_Voltage = models.CharField(max_length=200,blank=True,default="")
    Operating_Current = models.CharField(max_length=200,blank=True,default="")
    Lens_Colour = models.CharField(max_length=200,blank=True,default="")
    Lens_Shape = models.CharField(max_length=200,blank=True,default="")
    Lens_Material = models.CharField(max_length=200,blank=True,default="")
    Lens_Optics = models.CharField(max_length=200,blank=True,default="")
    Colour_Of_light = models.CharField(max_length=200,blank=True,default="")
    Front_Bezel_Colour = models.CharField(max_length=200,blank=True,default="")
    Front_Bezel_Material = models.CharField(max_length=200,blank=True,default="")
    Front_Ring_Colour = models.CharField(max_length=200,blank=True,default="")
    Front_Ring_Material = models.CharField(max_length=200,blank=True,default="")
    Contact = models.CharField(max_length=200,blank=True,default="")
    Contact_Material = models.CharField(max_length=200,blank=True,default="")
    Switching_Action = models.CharField(max_length=200,blank=True,default="")

    def __str__(self):
        return self.name

# creating model for clients database
class clientsM(models.Model):
    # id = models.IntegerField(primary_key=True)
    logo = models.ImageField(upload_to='clients/logos')
    companyName = models.CharField(max_length=200)

# creates model for certificats in database
class certificatsM(models.Model):
    certificateimage = models.ImageField(upload_to='certificats/image')
    certificatePDF = models.FileField(upload_to='certificats/pdf')
    certificateInfo = models.CharField(max_length=300)
