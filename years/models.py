from django.db import models

# Create your models here.
class yearsschool(models.Model):
    name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.name
    
    
class levelschool(models.Model):
    name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.name