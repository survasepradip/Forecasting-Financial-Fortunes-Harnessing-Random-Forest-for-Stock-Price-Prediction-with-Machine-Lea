from django.db import models
from django.conf import settings
from django.contrib.auth.models import  User, auth
# Create your models here.




class stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null= True  )
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    content = models.TextField()
    