from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields =('firstname','lastname')
        fields = '__all__'



# class EmployeeSerializer(serializers.Serializer):
#     firstname = serializers.CharField(max_length=10)
#     lastname = serializers.CharField(max_length=10)
#     emp_id = serializers.IntegerField()
#     email = serializers.EmailField(max_length=10)
#     date = serializers.DateTimeField()
#
#
#     def create(self, validated_data):
#         return Employees.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.firstname=validated_data.get('firstname',instance.firstname)
#         instance.lastname=validated_data.get('lastname',instance.lastname)
#         instance.emp_id=validated_data.get('emp_id',instance.emp_id)
#         instance.email=validated_data.get('email',instance.email)
#         instance.date=validated_data.get('date',instance.date)
#         instance.save()
#         return instance



