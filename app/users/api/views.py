from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CourseProgressSerializer
from app.courses.models import Course, CourseProgress


class CourseProgressListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseProgressSerializer
    queryset = CourseProgress.objects.all()

    def get_queryset(self):
        return CourseProgress.objects.filter(user=self.request.user)


class CourseProgressDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseProgressSerializer
    queryset = CourseProgress.objects.all()

    def get_queryset(self):
        return CourseProgress.objects.filter(user=self.request.user)
