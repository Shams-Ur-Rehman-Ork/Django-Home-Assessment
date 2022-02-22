from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'job', 'department', 'salary', 'hire_date']

    def validate(self, data):
        if not data['salary'] >= 0:
            raise serializers.ValidationError("Salary cannot be a negative number.")
        return data
