from django.shortcuts import render
from django.http import request
from django.template import context
from django.conf import settings
import json
from .forms import *
# Create your views here.

def index(request):
    return render(request,'home/index.html')

def index1(request):
    form = teacher_view()
    if request.method=="POST":
        form = teacher_view(request.POST)
        if form.is_valid():
            l = [form.cleaned_data['teacher_code'],form.cleaned_data['subject_code']]
            return timetable_t(request,l) 

    return render(request,'home/index3.html',{'form':form})

def index2(request):
    form = student_view()
    if request.method=="POST":
        form = student_view(request.POST)
        if form.is_valid():
            l = [form.cleaned_data['semester'],form.cleaned_data['Batch'],form.cleaned_data['subject_code']]
            return timetable_s(request,l)
    return render(request,'home/index2.html',{'form':form})
def timetable_t(request,x=[]):
    with open('staticfiles/TTEVENSEM2023.json','r') as user_file:
        file_contents=user_file.read()
    
    data = json.loads(file_contents)
    l = [{"Column1":"MON","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"TUE","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"WED","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"THU","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"FRI","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"SAT","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        ]
    list1 = ["MON","TUE","WED","THU","FRI","SAT"]
    dic = {"MON":0,"TUE":1,"WED":2,"THU":3,"FRI":4,"SAT":5}
    count = 0
    l1 = ["BTECH 2 SEM","BTECH 4 SEM","BTECH 6 SEM", "BTECH 8 SEM"]
    if x[1]=="":
        for t in l1:
            content = data[t]
            for i in content:
                if i is None:
                    break
                for k in i:
                    if isinstance(i[k],int):
                        pass
                    else:
                        str1 ="("+ x[0]+")"
                        
                        if i[k] in list1:
                            count = dic[i[k]]
                        if str1 in i[k]:
                            a = k
                            l[count].update({k:i[k]})

    elif x[0]=="":
        str1 = x[1]
        print(str1)
        for t in l1:
            content = data[t]
            for i in content:
                if i is None:
                    break
                for k in i:
                    if isinstance(i[k],int):
                        pass
                    else:
                        if i[k] in list1:
                            count = dic[i[k]]
                        if str1 in i[k]:
                            a = k
                            l[count].update({k:i[k]})
    else:
        str1 = x[0]
        str2 = x[1]
        for t in l1:
            content = data[t]
            for i in content:
                if i is None:
                    break
                for k in i:
                    if isinstance(i[k],int):
                        pass
                    else:
                        if i[k] in list1:
                            count = dic[i[k]]
                        if str1 in i[k] and str2 in i[k]:
                            a = k
                            l[count].update({k:i[k]})


    return render(request,'home/time.html',{"d":l})
def timetable_s(request,x=[]):
    with open('staticfiles/TTEVENSEM2023.json','r') as user_file:
        file_contents=user_file.read()
    
    data = json.loads(file_contents)
    if x[0] !="":    
        a= x[0]
        stri = "BTECH "+a+" SEM"
        content = data[stri]
    l = [{"Column1":"MON","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"TUE","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"WED","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"THU","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"FRI","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        {"Column1":"SAT","Column2":" ","Column3":" ","Column4":" ","Column4":" ","Column5":" ","Column6":" ","Column7":" ","Column8":" ","Column9":" ","Column10":" ",},
        ]
    list1 = ["MON","TUE","WED","THU","FRI","SAT"]
    dic = {"MON":0,"TUE":1,"WED":2,"THU":3,"FRI":4,"SAT":5}
    count = 0
    l1 = ["BTECH 2 SEM","BTECH 4 SEM","BTECH 6 SEM", "BTECH 8 SEM"]

    str2 = x[1]
    str3 = x[2]
    if x[0] != "":
        for i in content:
            for k in i:
                if isinstance(i[k],int):
                    pass
                else:
                    if i[k] in list1:
                        count = dic[i[k]]
                    if  str2 in i[k] and str3 in i[k]:
                        a = k
                        l[count].update({k:i[k]})
    else:
        for t in l1:
            content = data[t]
            for i in content:
                if i is None:
                    break
                for k in i:
                    if isinstance(i[k],int):
                        pass
                    else:
                        if i[k] in list1:
                            count = dic[i[k]]
                        if str2 in i[k] and str3 in i[k]:
                            a = k
                            l[count].update({k:i[k]})


    return render(request,'home/time.html',{"d":l})

