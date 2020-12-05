from django.contrib import admin
from .models import Category, Course, CourseProgress, Chapter


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]


class ChapterInline(admin.TabularInline):
    model = Chapter


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]
    list_display = ["title", "is_active"]


@admin.register(CourseProgress)
class CourseProcessAdmin(admin.ModelAdmin):
    list_display = ["course", "user"]
