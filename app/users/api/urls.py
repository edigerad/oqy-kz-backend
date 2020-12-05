from django.urls import path
from .views import CourseProgressListView, CourseProgressDetailView

urlpatterns = [
    path('courses/', CourseProgressListView.as_view()),
    path('courses/<int:pk>/', CourseProgressDetailView.as_view()),
]
