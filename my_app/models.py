from django.db import models

# Create your models here.
class user(models.Model):
   username=models.CharField(max_length=255)
   age=models.IntegerField()
   email=models.EmailField(max_length=255)
   password=models.CharField(max_length=255)
  

class Contact(models.Model):
   name=models.CharField(max_length=255)
   email=models.EmailField(max_length=255)
   subject=models.CharField(max_length=255)
   message=models.TextField()


class services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(default='')
    cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return (self.name)

    
   
   


   