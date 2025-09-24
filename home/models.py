# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    tip-blance = models.IntegerField(null=True, blank=True)
    sender_id = models.TextField(max_length=255, null=True, blank=True)
    send-amount = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Profiles(models.Model):

    #__Profiles_FIELDS__
    id = models.BooleanField()
    username = models.TextField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    descrption = models.TextField(max_length=255, null=True, blank=True)

    #__Profiles_FIELDS__END

    class Meta:
        verbose_name        = _("Profiles")
        verbose_name_plural = _("Profiles")



#__MODELS__END
