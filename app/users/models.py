from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField, BooleanField, ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django.core.validators import RegexValidator

PHONE_REGEX = RegexValidator(regex=settings.ACCOUNT_PHONE_REGEX,
                             message=settings.ACCOUNT_PHONE_REGEX_MESSAGE)

NAME_REGEX = RegexValidator(regex='^[^{}]'.format(settings.ACCOUNT_SYMBOLS_REGEX),
                            message=_("Name is not correct!"))


class User(AbstractUser):
    phone_number = CharField(_('Phone number'), validators=[PHONE_REGEX], max_length=11, db_index=True, unique=True)
    fullname = CharField(_("Full name"), validators=[NAME_REGEX], max_length=70)
    avatar = ImageField(_('Avatar'), null=True, blank=True)
    email = EmailField(_('Email address'), blank=True, null=True)
    email_verified = BooleanField(_('Email verified'), default=False)
    verified_at = models.DateTimeField(_('Verified at'), blank=True, null=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('fullname', 'phone_number')

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
