from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=100)
    price = models.IntegerField(default=0) 
    user=models.ForeignKey(User,on_delete=models.CASCADE) #needtochange
    description=models.TextField()
    
    def __str__(self):
        return str(self.pk)+'-'+str(self.name)