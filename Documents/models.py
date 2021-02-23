from django.contrib.auth.models import User
from django.db import models

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=50,null=True)
    branch = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Documents(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.DateField(auto_now_add=True)
    branch = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    documentfile = models.FileField(null=True)
    filetype = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status