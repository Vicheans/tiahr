from django.urls import path
from . import views

urlpatterns = [
    path("employee/", views.EmployeeListCreate.as_view(), name="employee-view-create"),
    path(
        "employee/<int:pk>/",
        views.EmployeeRetrieveUpdateDestory.as_view(),
        name="employee-update",
    ),
]