from django.urls import path
from . import views

urlpatterns = [
    path("leave/", views.LeaveListCreate.as_view(), name="leave-view-create"),
    path(
        "leave/<int:pk>/",
        views.LeaveRetrieveUpdateDestory.as_view(),
        name="leave-update",
    ),
]