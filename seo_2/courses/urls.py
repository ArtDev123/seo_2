from django.urls import path
from . import views

urlpatterns = [
    path('mine/',
         views.ManageCourseList.as_view(),
         name = 'manage_course_list'),
    path('create/',
         views.CourseCreateView.as_view(),
         name = 'course_create'),
    path('<pk>/edit/',
         views.CourseUpdateView.as_view(),
         name = 'course_esit'),
    path('<pk>/delete',
         views.DeleteView.as_view(),
         name = 'course_delete'),
]