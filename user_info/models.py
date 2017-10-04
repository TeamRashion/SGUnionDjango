from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey('auth.User')
    user_name = models.CharField(max_length=20)
    user_pic = models.FileField()


    def __str__(self):
        return str(self.user_idx)


    def getUserName(self):
        return str(self.user_name)


class UserEmail(models.Model):
    user = models.ForeignKey('auth.User')
    email = models.CharField(max_length=20)


    def __str__(self):
        return str(self.email)
