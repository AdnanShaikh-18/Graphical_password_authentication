from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# these models / databses are for the colors

class Color1(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to='images/color1/')

    def __str__(self):
        return self.name

class Color2(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to='images/color2')

    def __str__(self):
        return self.name

class Color3(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to='images/color3')

    def __str__(self):
        return self.name

#################################################



class Profile(models.Model):

    user=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    social_media_url=models.CharField(max_length=50, blank=True,null=True)
    bio=models.TextField(blank=True)
    gender=models.CharField(max_length=10,default='male')
    color1=models.CharField(max_length=50)
    color2=models.CharField(max_length=50)
    color3=models.CharField(max_length=50)

    def __str__(self):
        return self.user+  self.color1
    



class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    body=models.TextField(null=False,blank=False)
    
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=100,null=True,blank=True,default='error 404 bio not found')
    github_id=models.URLField(blank=True,null=True,max_length=100)
    insta_id=models.URLField(blank=True,null=True,max_length=100)
    twitter_id=models.URLField(blank=True,null=True,max_length=100)
    yt_id=models.URLField(blank=True,null=True,max_length=100)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    name=models.CharField(max_length=260)
    roll=models.IntegerField()

    def __str__(self):
        return self.name


    







