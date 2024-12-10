from django.urls import path
from . import views

urlpatterns = [
    path("attendance/", views.AttendanceListCreate.as_view(), name="attendance-view-create"),
    path(
        "attendance/<int:pk>/",
        views.AttendanceRetrieveUpdateDestory.as_view(),
        name="attendance-update",
    ),
]