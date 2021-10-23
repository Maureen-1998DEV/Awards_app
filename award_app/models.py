from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio =models.CharField(max_length=300)
    Profile_pic = models.ImageField(upload_to='profile/')
    pub_date = models.DateTimeField(auto_now_add=True)