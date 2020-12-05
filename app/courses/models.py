from django.db import models
from app.common import models as c_models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class Category(c_models.TitleBaseModel,
               c_models.ActivationBaseModel):
    class Meta:
        verbose_name = _('category', )
        verbose_name_plural = _('categories', )


class Course(c_models.TitleDescriptionBaseModel,
             c_models.TimeStampedModel,
             c_models.LanguageBaseModel,
             c_models.ActivationBaseModel
             ):
    category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='course_category',
                                 on_delete=models.CASCADE)
    teacher = models.CharField(_('Teacher'), max_length=150)
    requirements = models.TextField(_('Requirements'), blank=True, null=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='course_author',
        blank=True,
        on_delete=models.CASCADE
    )
    cover_image = models.ImageField(_('Cover image'), )

    registered_count = models.BigIntegerField(_('Registration count'), default=0)

    class Meta:
        verbose_name = _('course', )
        verbose_name_plural = _('courses', )
        ordering = ('-created',)

    def increase_registered(self):
        self.registered_count += 1
        self.save()

    def decrease_registered(self):
        self.registered_count -= 1
        self.save()

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()


class Chapter(c_models.TitleDescriptionBaseModel):
    order = models.PositiveSmallIntegerField(_('Order'), default=0, editable=False, db_index=True)
    course = models.ForeignKey(Course, verbose_name=_('Course'), related_name='chapters', on_delete=models.CASCADE)
    content = RichTextUploadingField(verbose_name=_('Content'), )

    class Meta:
        verbose_name = _('Chapter', )
        verbose_name_plural = _('Chapter', )
        ordering = ('order',)


class CourseProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=_('Course'), related_name='registered', on_delete=models.CASCADE)
    registered = models.DateTimeField(verbose_name=_('Registered'), auto_now_add=True)
    is_active = models.BooleanField(verbose_name=_('Is active'), default=False)
    is_finished = models.BooleanField(verbose_name=_('Is finished'), default=False)

    class Meta:
        verbose_name = _('course progress', )
        verbose_name_plural = _('course progresses', )
        unique_together = ('user', 'course')
        ordering = ('-registered',)

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()
