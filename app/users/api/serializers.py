from rest_framework import serializers

from app.courses.api.serializers import CategorySerializer
from app.courses.models import Course, Chapter, CourseProgress


class ChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('order', 'title', 'description', 'content')


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    chapters = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'category', 'chapters')

    def get_chapters(self, obj):
        qs = Chapter.objects.filter(course=obj)
        return ChapterDetailSerializer(qs, many=True).data


class CourseProgressSerializer(serializers.ModelSerializer):
    course = CourseDetailSerializer()

    class Meta:
        model = CourseProgress
        fields = ('course', 'registered')
