from django.shortcuts import render
from student.models import Student,Login,Mark
from django.core.files.storage import FileSystemStorage
# Create your views here.
def student_registration(request):
    if request.method=="POST":
        obj=Student()
        obj.first_name=request.POST.get('txt_firstname')
        obj.middle_name=request.POST.get('txt_middlename')
        obj.last_name=request.POST.get('txt_lastname')
        obj.dob=request.POST.get('dob')
        obj.phone_number=request.POST.get('txt_phone')
        myfile = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        obj.image = myfile.name
        obj.save()

        ob=Login()
        ob.username=request.POST.get('txt_phone')
        ob.password=request.POST.get('txt_password')
        ob.u_id=obj.s_id
        ob.type="student"
        ob.save()
        objlist = "Student Details Registered Successfully..  "
        context = {
            'msg': objlist
        }
        return render(request, 'student/Student Registration.html', context)
    return render(request,'student/Student Registration.html')




def admin(request):
    if request.method=="POST":

        if Login.objects.filter(type='admin').exists():
            print("fg")
            msg="ADMIN already registered...!!!"
            context={
                'alert':msg
            }
            return render(request,'student/Admin Registration.html',context)
        else:
            obj=Login()
            obj.username=request.POST.get('txt_firstname')
            obj.password=request.POST.get('txt_password')
            obj.type="admin"
            obj.u_id=1
            obj.save()
    return render(request,'student/Admin Registration.html')



def view_student(request):
    objlist=Student.objects.all()
    context={
        'obval':objlist
    }
    return render(request,'student/View Student details.html',context)



def add_mark(request):
    objlist=Student.objects.all()
    context={
        'obval':objlist,
    }
    if request.method=="POST":
        obb=Mark()
        obb.s_id=request.POST.get('stname')
        obb.assignment=request.POST.get('txt_assgnmnt')
        obb.attendance=request.POST.get('txt_attndance')
        obb.series_test=request.POST.get('txt_st')
        assign = request.POST.get('txt_assgnmnt')
        attendence = request.POST.get('txt_attndance')
        series_test = request.POST.get('txt_st')
        tot = int(assign) + int(attendence) + int(series_test)
        obb.total = tot
        obb.save()
    return render(request,'student/Add mark.html',context)



def view_mark(request):
    objlist=Mark.objects.all()
    context={
        'obval':objlist
    }
    return render(request,'student/View mark details and edit.html',context)

def edit_mark(request,idd):
    objlist=Mark.objects.filter(m_id=idd)
    context={
        'obval':objlist,
    }
    if request.method=="POST":
        ob=Mark.objects.get(m_id=idd)
        ob.assignment = request.POST.get('txt_assgnmnt')
        ob.attendance = request.POST.get('txt_attndance')
        ob.series_test = request.POST.get('txt_st')
        assign = request.POST.get('txt_assgnmnt')
        attendence = request.POST.get('txt_attndance')
        series_test = request.POST.get('txt_st')
        tot = int(assign) + int(attendence) + int(series_test)
        ob.total = tot
        ob.save()
        return view_mark(request)
    return render(request,'student/Edit mark.html',context)



def update(request):
    idd=request.session["u_id"]
    obb=Student.objects.filter(s_id=idd)
    obj=Login.objects.filter(u_id=idd,type='student')
    context={
        'obval':obb,
        'oval':obj
    }
    if request.method=="POST":
        ob=Student.objects.get(s_id=idd)
        ob.first_name = request.POST.get('txt_firstname')
        ob.middle_name = request.POST.get('txt_middlename')
        ob.last_name = request.POST.get('txt_lastname')
        ob.dob = request.POST.get('dob')
        ob.phone_number = request.POST.get('txt_phone')
        myfile = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        ob.image = myfile.name
        ob.save()

        obk = Login.objects.get(u_id=idd,type='student')
        obk.username = request.POST.get('txt_phone')
        obk.password = request.POST.get('txt_password')
        obk.u_id=idd
        obk.save()
    return render(request,'student/Update profile.html',context)