from rest_framework import serializers

from app.courses.models import Category, Course, Chapter


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'is_active')


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('order', 'title', 'description')


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    chapters = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'category', 'chapters', 'cover_image', 'registered_count')

    def get_chapters(self, obj):
        qs = Chapter.objects.filter(course=obj)
        return ChapterSerializer(qs, many=True).data
