from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class GenericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class=EmployeeSerializer
    queryset = Employee.objects.all()

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)


    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self, request, id):
        return self.destroy(request,id)


class employee(APIView):

    def get(self, request):
        employees1 = Employee.objects.all()
        serializer = EmployeeSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self,request):
        print("Entered")
        print("printing data")
        data=request.data
        print(data)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class employeeById(APIView):

    def get(self,request,pk):
        print(pk)
        try:
            employee = Employee.objects.get(pk=pk)
            print("printing employee")
            print(employee)
        except Employee.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        serializer= EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self,request,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        data=request.data
        serializer=EmployeeSerializer(employee,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class EmployeeViewSet(viewsets.ViewSet):

    def list(self,request):
        employees1 = Employee.objects.all()
        serializer = EmployeeSerializer(employees1, many=True)
        return Response(serializer.data)

    def create(self,request):
        data = request.data
        print(data)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset,pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def update(self,request,pk=None):
        employee = self.get_object(pk=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)









