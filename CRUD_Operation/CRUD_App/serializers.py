from rest_framework import serializers
from .models import *
from .validation import *
from datetime import date

class Student_serilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_student_no(self, value):
        print("value",value)
        if value != "":
            if not number.match(str(value)):
                raise serializers.ValidationError("Enter Valid Number")
        return value    

    def validate_student_name(self, value):
        print("value",value)
        if value != "":
            if not text_space.match(value):
                raise serializers.ValidationError("Enter Valid Name")
        return value

    def validate_student_dob(self, value):
        print("value",value)
        if not dateFormat.match(str(value)):
            raise serializers.ValidationError("Enter Valid DOB")
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if (age < 4):
            raise serializers.ValidationError("Enter Valid DOB above 4 years")    
        return value

    def validate_student_doj(self, value):
        print("value",value)
        if value != "":
            if not dateFormat.match(str(value)):
                raise serializers.ValidationError("Enter Valid Date")
        return value         

    def validate(self, data):
        today = date.today()
        if data['student_dob'] != None and data['student_doj'] != None:
            dob = data['student_dob']
            print(dob)
            doj = data['student_doj']
            print(doj)
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            print(age)
            doj_age = doj.year - dob.year - ((doj.month, doj.day) < (dob.month, dob.day))
            print(doj_age)
            if (age < 4):
                raise serializers.ValidationError("Enter Valid DOB")

            if (doj_age < 4):
                raise serializers.ValidationError("Enter Valid DOJ")
    
        return data       