from django.urls import path
from . import views

urlpatterns = [
    path("department/", views.DepartmentListCreate.as_view(), name="department-view-create"),
    path(
        "department/<int:pk>/",
        views.DepartmentRetrieveUpdateDestory.as_view(),
        name="department-update",
    ),
]