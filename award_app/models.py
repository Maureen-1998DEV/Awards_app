from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator,MaxValueValidator 
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio =models.CharField(max_length=300)
    profile_pic = CloudinaryField('profile/')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
    
    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(title__icontains=search_term)
        return profiles

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
       if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()

class Project(models.Model):
    
    project_name = models.CharField(max_length=30)
    image = CloudinaryField('images/')
    recorded_demo = models.FileField(upload_to='documents/' , null=True)
    project_description = models.CharField(max_length=3000)
    
    project_url = models.CharField(max_length=70)
    technologies_used = models.CharField(max_length=70)

    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    posted_time = models.DateTimeField(auto_now_add=True,)
    

    class Meta:
        ordering = ['-posted_time']

    def save_projects(self):
        self.save()
    
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

class Comments(models.Model):
    comment = models.CharField(max_length = 300)
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_by_projects(cls, id):
        comments = Comments.objects.filter(project__pk = id)
        return comments

class Votes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post =  models.ForeignKey(Project,on_delete=models.CASCADE,related_name='likes')
    design = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    creativity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    content = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
