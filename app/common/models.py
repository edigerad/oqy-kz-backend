from django.db import models
from django.utils import timezone
from django.utils.translation import get_language_info
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ("en", _(get_language_info("en")["name"])),
    ("ru", _(get_language_info("ru")["name"])),
    ("kk", _(get_language_info("kk")["name"])),
)

COURSE_LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
    ("kk", _("Kazakh")),
)


# ABSTRACT CLASSES
class MyDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        if (
                self.auto_now or (self.auto_now_add and add)
        ) and model_instance.is_modified:
            value = timezone.now()
            setattr(model_instance, self.attname, value)
            return value
        return models.Field.pre_save(self, model_instance, add)


class LanguageBaseModel(models.Model):
    lang = models.CharField(
        _("Language"), choices=COURSE_LANGUAGES, max_length=2, default="en"
    )

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_("Created"), auto_now_add=True, db_index=True)
    modified = MyDateTimeField(_("Modified"), auto_now=True)
    __is_modified = True

    @property
    def is_modified(self):
        return self.__is_modified

    @property
    def ago(self):
        return (timezone.now() - self.created).total_seconds()

    @is_modified.setter
    def set_modified(self, value):
        self.__is_modified = value

    class Meta:
        abstract = True
        ordering = ["-created"]

    def __str__(self):
        return "{} {}".format(self.created, self.modified)


class ActivationBaseModel(models.Model):
    is_active = models.BooleanField(_("Is active?"), default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.is_active)

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()


class TitleBaseModel(models.Model):
    title = models.CharField(_("Title"), max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.title)


class TextBaseModel(models.Model):
    text = models.TextField(
        _("Text"),
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.text)


class DescriptionBaseModel(models.Model):
    description = models.TextField(_("Description"), blank=True, default="")

    class Meta:
        abstract = True


class TitleDescriptionBaseModel(TitleBaseModel, DescriptionBaseModel):
    class Meta:
        abstract = True
