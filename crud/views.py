from django.shortcuts import render
from .serializer import Studentserilaiser
from .models import Student
from rest_framework.response import Response
from rest_framework import status,viewsets



class Student_view(viewsets.ViewSet):
    def list(self,request):
        print('*********list*********')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)

        stu = Student.objects.all()
        serialiser = Studentserilaiser(stu,many=True)
        return Response(data=serialiser.data)
    
    def retrieve(self,request,pk=None):
        print('*********retrieve*********')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)

        id = pk 
        if id is not None:
            stu = Student.objects.get(id= id)
            seriliser = Studentserilaiser(stu)
            return Response(seriliser.data)
    
    def create(self,request):
        print('*********create*********')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)

        seriliser = Studentserilaiser(data=request.data)
        if seriliser.is_valid():
            seriliser.save()
            return Response({'msg':'created successfully...'},status=status.HTTP_201_CREATED)
        return Response(seriliser.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def update(self,request,pk=None):
        print('*********update*********')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)

        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serilaiser = Studentserilaiser(stu,data=request.data)
            if serilaiser.is_valid():
                serilaiser.save()
                return Response({'msg':'update successfull'},status=status.HTTP_200_OK)
            return Response(serilaiser.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk=None):
        print('*********partial_update*********')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)

        id=pk
        if id is not None:
            stu = Student.objects.get(id=id)
            seriliser = Studentserilaiser(stu,data=request.data,partial = True)
            if seriliser.is_valid():
                seriliser.save()
                return Response({'msg':'partial update done...'},status=status.HTTP_200_OK)
            return Response(seriliser.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        print('*********delete*********')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)

        id= pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({'msg':'delete successfull'},status=status.HTTP_200_OK)
        return Response({'msg':'not acailable...'},status=status.HTTP_400_BAD_REQUEST)


    
    


        


        




# Create your views here.
