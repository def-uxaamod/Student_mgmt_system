from django.shortcuts import render
from mgmt_app.models  import Student
from django.http import HttpResponseRedirect

# Create your views here.

def home_page(request):
    return render(request,"home_page.html")

def entry_details(request):
    if request.method=="GET":
        return render(request,"details.html")
    else:
        Student.objects.create(name=request.POST['name'],email=request.POST['email'],age=request.POST['age'])
        return HttpResponseRedirect("/")
    
def see_details(request):
    students = Student.objects.all()
    return render(request,"see.html",{'s':students})
def update_details(request,id):
    if request.method=="GET":
        student = Student.objects.get(id=id)
        return render(request,"update.html",{'s':student})
    else:
        student = Student.objects.get(id=id)
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.save()
        return HttpResponseRedirect("/")
def delete_details(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect("/")