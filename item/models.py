from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CatagoryModel(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']

class ItemModel(models.Model):
    catagory=models.ForeignKey(CatagoryModel,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    price=models.FloatField()
    isSold=models.BooleanField(default=False)
    creator=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="uploads")
    def __str__(self):
        return self.name
   