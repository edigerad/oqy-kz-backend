from django.db.models.signals import post_save
from django.dispatch import receiver

from app.courses.models import CourseProgress


@receiver(post_save, sender=CourseProgress)
def course_progress_post_save(sender, instance, *args, **kwargs):
    instance.course.registered_count += 1
    instance.course.save(update_fields=['registered_count'])
