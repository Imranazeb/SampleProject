import os

import shortuuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from PIL import Image
from shortuuid.django_fields import ShortUUIDField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/username_<id>/filename
    filename = os.path.basename(filename)
    return f"{instance.full_name}_{instance.id}/{filename}"


class User(AbstractUser):
    id = ShortUUIDField(
        primary_key=True,
        editable=False,
        length=5,
        max_length=15,
        alphabet="abcdefghijklmnopqrstuvwxyz",
    )
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "username"]

    def __str__(self):
        return self.username


class Profile(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)

    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to=user_directory_path,
        default="images/profiles/default.jpg",
    )

    def thumbnail(self):
        return mark_safe(
            '<img src="/media/%s" width="50" height="50" object-fit:"cover" style="border-radius: 5px;" />'
            % (self.profile_image)
        )

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            id=instance.id,
            full_name=instance.full_name,
            email=instance.email,
        )


def save_user_profile(sender, instance, *args, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
