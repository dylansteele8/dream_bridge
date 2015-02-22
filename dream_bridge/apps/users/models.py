from django.db import models
from django.contrib.auth.models import User
import uuid, os

class Profile(models.Model):

  # Fields
  user = models.OneToOneField(User)

  role = models.CharField(
    max_length=2,
    choices=(('U', 'User'),
             ('A', 'Admin')),
    blank=False,
    default="G"
  )

  avatar = models.ImageField(
    upload_to=lambda i, filename: os.path.join('avatars', "%s.%s" % (uuid.uuid4(), filename.split('.')[-1])),
    blank=True,
    default=""
  )

  joined_timestamp = models.DateTimeField(
    auto_now_add=True,
    editable=False
  )

  def __str__(self):
    return self.user.first_name+" "+self.user.last_name

  def name(self):
    return self.user.first_name+" "+self.user.last_name

class Company(models.Model):

  name = models.CharField(max_length=99)

  def __str__(self):
    return self.name


class Job(models.Model):

  title = models.CharField(max_length=99)
  company = models.OneToOneField(Company)
  location = models.CharField(max_length=99)
  interested_users = models.ManyToManyField(User)
  video = models.FileField(
    upload_to=lambda i, filename: os.path.join('job-videos', "%s.%s" % (uuid.uuid4(), filename.split('.')[-1])),
    default=""
  )

  def __str__(self):
    return self.title


class UserDVideo(models.Model):

  user = models.ForeignKey('UserD')
  video = models.FileField(
    upload_to=lambda i, filename: os.path.join('user-videos', "%s.%s" % (uuid.uuid4(), filename.split('.')[-1])),
    default=""
  )

  def __str__(self):
    return self.user.name + "-video"

class UserD(models.Model):

  name = models.CharField(max_length=99)
  email = models.CharField(max_length=99)
  school = models.CharField(max_length=99)
  gpa = models.CharField(max_length=4)
  major = models.CharField(max_length=99)
  interested_jobs = models.ManyToManyField(Job)
  resume = models.ImageField(
    upload_to=lambda i, filename: os.path.join('resume', "%s.%s" % (uuid.uuid4(), filename.split('.')[-1])),
    blank=True,
    default=""
  )
  description = models.CharField(max_length=999)
  languages_known = models.CharField(max_length=999)

  def __str__(self):
    return self.name
