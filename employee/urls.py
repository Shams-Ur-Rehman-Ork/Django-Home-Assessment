from django.urls import path
from .views import EmployeeAPIView, SingleEmployeeAPIView

urlpatterns = [
    path("", EmployeeAPIView.as_view(), name="Listing-employees"),
    path("<int:pk>/", SingleEmployeeAPIView.as_view(), name="Retrieve-single-employee")
]
