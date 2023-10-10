from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee
from .serailizer import EmployeeSerializer
# Create your views here.

class EmployeeDetail(APIView):
    def get(self,request):
        obj = Employee.objects.all()
        serialzier = EmployeeSerializer(obj, many=True)
        return Response(serialzier.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serialzier= EmployeeSerializer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data,status=status.HTTP_201_CREATED)
        return Response(serialzier.data, status=status.HTTP_400_BAD_REQUEST)

class EmployeeInfo(APIView):
    def get(self,request,id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msz={"msz":"not found"}
            return Response(msz, status=status.HTTP_404_NOT_FOUND)
        
        serialzier = EmployeeSerializer(obj)
        return Response(serialzier.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj= Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msz={"msz":"Notfound Error"}

            return Response(msz,status=status.HTTP_404_NOT_FOUND)
        
        serialzier = EmployeeSerializer(obj,data=request.data)

        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serialzier.errors,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            obj=Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msz={"msz":"not found"}
            return Response(msz,status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msz":"deleted"},status=status.HTTP_204_NO_CONTENT)
    
    
    