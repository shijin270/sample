from django.shortcuts import render
from student.models import Login

# Create your views here.
def admin_home(request):
    return render(request,'temp/admin.html')

def student_home(request):
    return render(request,'temp/student.html')

def login(request):
    if request.method == "POST":
        uname = request.POST.get("unmae")
        passw = request.POST.get("pass")
        obj = Login.objects.filter(username=uname, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["u_id"] = uid
                return render(request, 'temp/admin.html')
            elif tp == "student":
                request.session["u_id"] = uid
                return render(request, 'temp/student.html')
            # elif tp == "subadmin":
            #     request.session["uid"] = uid
            #     return render(request, 'login/s_subhome.html')
            # else:
        objlist = "Username or Password incorrect... Please try again...!"
        context = {
            'msg': objlist,
        }
        return render(request, 'temp/login1.html', context)
    return render(request,'temp/login1.html')


def add(request):
    return render(request, 'temp/admin registration.html')


def stu(request):
    return render(request, 'temp/student registration.html')