from django.db import models
from django.contrib.auth import get_user_model
# for genrating unique id (long charaters)
import uuid
from datetime import datetime

User=get_user_model() # get the model of current logged in user 

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(null=True)
    profileImg=models.ImageField(upload_to='profile_images',default="defaultProfile.png")
    location=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    # primary key
    # will generate unique numbers
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)

    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to="posts_images")
    caption=models.TextField
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user