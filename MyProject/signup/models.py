from django.db import models


class user  (models.Model):
    userId = models.PositiveSmallIntegerField
    username = models.CharField(max_length=15)
    email = models.EmailField
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    created_date = models.DateTimeField
    dob = models.DateField
    schoolname = models.CharField(max_length=100)
    grade = models.PositiveSmallIntegerField
    schooladdress = models.CharField(max_length=200)
    subjects = models.CharField(max_length=200)
    lastmodified_date = models.DateTimeField

    def __str__(self):
        return str(self.userId)


class ProjectMaster(models.Model):
    pId = models.PositiveSmallIntegerField(auto_created=True)
    projectname = models.CharField(max_length=200)
    student = models.PositiveSmallIntegerField
    studentgrade = models.PositiveSmallIntegerField
    created_date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200)
    lastmodified_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.pId) + " " + self.projectname + " " + self.tags
