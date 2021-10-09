from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query_utils import Q
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.

def student_view(request):
    # if request.method == "GET":
    return render(request, "student.html")

@api_view(['POST'])
def student_details_post_api_view(request):
    serializer = Student_serilizer(data=request.data)
    if serializer.is_valid():
        student_no = (serializer.validated_data["student_no"])
        if student_no != "":
            stud_data = Student.objects.filter(student_no=student_no).exists()
        print("data=", student_no, stud_data)
        if stud_data and student_no != "":
            return Response(data={"non_field_errors": "Student No. Already Exists..."},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def student_list_view(request):
    context = {}
    if request.method == 'GET':
        today = date.today()
        context['date'] = today.strftime("%d/%m/%Y")
        stud = Student.objects.all()
        context['stud_data'] = stud

        search = request.GET.get("search", None)
        plc = request.GET.get("page_list_count", None)
        page_no = request.GET.get("page", 1)

        print(plc)
        print(page_no)
        

        if search:
            context['search'] = search
            
            print(search)
            if '/' in search:
                dt = datetime.strptime(search, '%d/%m/%Y').date()
                dt1 = datetime.strptime(search, '%d/%m/%Y').date()
                stud = stud.filter(Q(student_name__icontains=search) | Q(student_no__icontains=search) | Q(student_dob__icontains=dt) | Q(student_doj__icontains=dt1))
            else:
                stud = stud.filter(Q(student_name__icontains=search) | Q(student_no__icontains=search))
            print(stud)
        if plc:
            context['plc'] = plc
            p = Paginator(stud, plc)
        else:
            p = Paginator(stud, 10)
            context['plc'] = 10

        try:
            page = p.page(page_no)
        except:
            page = p.page(1)

        context["Student"] = page
        return render(request, 'student_list.html', context) 


def student_details_update(request,id):
    context = {}
    if request.method == 'GET':
        today = date.today()
        context['date'] = today.strftime("%d/%m/%Y")
        
        context['stud_data'] = Student.objects.filter(id=id)

        return render(request, 'student_update.html', context)

@api_view(['PATCH'])
def student_patch_api_view(request, pk):
    data = Student.objects.get(id=pk)
    serializer = Student_serilizer(data, data=request.data, partial=True)
    if serializer.is_valid():
        student_no = (serializer.validated_data["student_no"])
        if student_no != "":
            stud_data = Student.objects.filter(student_no=student_no).exists()
        print("data=", student_no, stud_data)
        if stud_data and student_no != "":
            return Response(data={"non_field_errors": "Student No. Already Exists..."},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def student_delete_api_view(request,id):
    bank_id = request.POST.get('id')
    print("bank_id==", bank_id)
    stud = Student.objects.get(id=id)
    if stud:
        stud.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
