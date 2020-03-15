from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url
from django.template.loader import render_to_string

from django.core.mail import send_mail
# Create your models here.


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', "남성"
        FEMALE = 'F', '여성'

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(
        validators=[
            RegexValidator(r"^\d{3}-?\d{3,4}-?\d{4}$")
        ],
        blank=True,
        max_length=13)
    gender = models.CharField(
        blank=True, choices=GenderChoices.choices, max_length=1)
    profile = models.ImageField(
        blank=True, upload_to="accounts/profile/%Y/%m/%d"
    )

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def avatar_url(self):
        if self.profile:
            return self.profile.url
        else:
            return resolve_url("pydenticon_image", self.username)

    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.html", {
            "user": self
        })
        content = render_to_string("accounts/welcome_email_content.html", {
            "user": self
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, sender_email, [
                  self.email], fail_silently=False)
