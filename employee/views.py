from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from .models import Employee
from .serializers import EmployeeSerializer
from .custom_response_handler import BaseAPIView


class EmployeeAPIView(BaseAPIView, ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        """API to get List of Employees"""
        response = self.list(request, *args, **kwargs)
        return self.send_success_response(message="List of Employees",
                                          payload=response.data)

    def post(self, request, *args, **kwargs):
        """Creating Employee record API"""
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.send_created_response(message="Employee created successfully.",
                                          payload=serializer.data)


class SingleEmployeeAPIView(BaseAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        """API to get single Employee by id"""
        try:
            response = self.retrieve(request, *args, **kwargs)
            return self.send_success_response(message="Employee data",
                                              payload=response.data)
        except Http404:
            return self.send_not_found_response()
        except Exception as err:
            print(err)
            return self.send_bad_request_response(message="An error occurred while getting employee record.")

    def put(self, request, *args, **kwargs):
        """Updating employee full record"""
        try:
            response = self.update(request, *args, **kwargs)
            return self.send_success_response(message="Employee updated successfully.",
                                              payload=response.data)
        except Http404:
            return self.send_not_found_response()
        except Exception as err:
            print(err)
            return self.send_bad_request_response(message="An error occurred while updating employee record.")

    def patch(self, request, *args, **kwargs):
        """Updating employee partial record."""
        try:
            response = self.partial_update(request, *args, **kwargs)
            return self.send_success_response(message="Employee updated successfully",
                                              payload=response.data)
        except Http404:
            return self.send_not_found_response()
        except Exception as err:
            print(err)
            return self.send_bad_request_response(message="An error occurred while updating employee record.")

    def delete(self, request, *args, **kwargs):
        """Deleting employee record."""
        try:
            response = self.destroy(request, *args, **kwargs)
            return self.send_success_response(message="Employee deleted successfully.",
                                              payload=response.data)
        except Http404:
            return self.send_not_found_response()
        except Exception as err:
            print(err)
            return self.send_bad_request_response(message="An unknown error occurred while deleting employee.")
