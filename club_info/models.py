from django.db import models

# Create your models here.

class ClubInfo(models.Model):
    club_name = models.CharField(max_length=20)
    description = models.TextField(default="", blank=True)


    def __str__(self):
        return str(self.club_name)


class MemberInfo(models.Model):
    user = models.ForeignKey('auth.User')
    club = models.ForeignKey('ClubInfo')

    def __str__(self):
        return str(self.user) + " in " + str(self.club);

    def getDescription(self):
        return str(self.description)


class AdminInfo(models.Model):
    user = models.ForeignKey('MemberInfo')
    type = models.IntegerField()
    admin_name = models.CharField(max_length=20)


    def __str__(self):
        return str(self.user)


    def getClubAdmin(self):
        return str(self.user.user)

