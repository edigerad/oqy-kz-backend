from django.urls import path
from .views import CategoryListView, CourseListView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryListView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>/', CourseListView.as_view()),
]
