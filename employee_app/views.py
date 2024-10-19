from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from employee_app.models import employee
from employee_app.models import student
from employee_app.models import teachers
from employee_app.models import degree
from employee_app.models import discipline
from employee_app.models import Class
from employee_app.models import Subject
from employee_app.models import School_system
from employee_app import models

# Create your views here.
def index(request):
    return render(request, 'first_one.html')

@csrf_exempt
def all_emp_controller(request):
    pass


@csrf_exempt
def add_deg(request):
    if request.method == 'GET':
        return render(request, 'degree_data.html')
    else:
        degree_name = request.POST.get('degree_name')
        msg = degree.objects.create(degree_name=degree_name)
        message = f"Degree has been stored as : {msg.degree_name}"
        return render(request, 'degree_data.html', {'msg':message})

@csrf_exempt
def update_controller(request,id=None):
    emp_data = models.employee.objects.all()
    if request.method == 'GET':
        return render(request, 'update_controller.html',{'msg': emp_data})
    else:
        updated_names = request.POST.get('employee_name')
        emp_controller = models.employee.objects.get(employee_id=id)
        emp_controller.employee_name = updated_names
        emp_controller.save()
        return render(request, 'update_controller.html',{'msg': emp_data})

@csrf_exempt
def update_std_controller(request,id=None):
    emp_data = models.student.objects.all()
    if request.method == 'GET':
        return render(request, 'std_update_delete_page.html',{'msg': emp_data})
    else:
        updated_names = request.POST.get('employee_name')
        std_controller = models.student.objects.get(student_id=id)
        std_controller.student_name = updated_names
        std_controller.save()
        return render(request, 'std_update_delete_page.html',{'msg': emp_data})

@csrf_exempt
def update_t_controller(request,id=None):
    emp_data = models.teachers.objects.all()
    if request.method == 'GET':
        return render(request, 't_update_del.html',{'msg': emp_data})
    else:
        updated_names = request.POST.get('t_name')
        t_controller = models.teachers.objects.get(teacher_id=id)
        t_controller.teacher_name = updated_names
        t_controller.save()
        return render(request, 't_update_del.html',{'msg': emp_data})

@csrf_exempt
def update_class_controller(request,id=None):
    emp_data = models.Class.objects.all()
    if request.method == 'GET':
        return render(request, 'delete_class.html',{'msg': emp_data})
    else:
        updated_names = request.POST.get('c_name')
        t_controller = models.Class.objects.get(class_id=id)
        t_controller.class_name = updated_names
        t_controller.save()
        return render(request, 'delete_class.html',{'msg': emp_data})

@csrf_exempt
def update_subject_controller(request,id=None):
    emp_data = models.Subject.objects.all()
    if request.method == 'GET':
        return render(request, 'up_dell.html',{'msg': emp_data})
    else:
        updated_names = request.POST.get('s_name')
        s_controller = models.Subject.objects.get(subject_id=id)
        s_controller.subject_name = updated_names
        s_controller.save()
        return render(request, 'up_dell.html',{'msg': emp_data})

@csrf_exempt
def sigup_controller(request):
    if request.method == 'GET':
        return render(request, 'signup_login_age.html')
    else:
        username = request.POST.get('username')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        confirm_pass = request.POST.get('conf_pass')
        if Password != confirm_pass:
            return render(request, 'signup_login_age.html', {'msg':'Password does not match'})
        else:
            models.user.objects.create(username=username, Email=Email, Password=Password, user_type='admin')
            return render(request, 'signup_login_age.html', {'msg':'User has been created successfully'})

@csrf_exempt
def SS_sigup_controller(request):
    if request.method == 'GET':
        return render(request, 'SS_signup.html')
    else:
        username = request.POST.get('username')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        confirm_pass = request.POST.get('conf_pass')
        if Password != confirm_pass:
            return render(request, 'signup_login_age.html', {'msg':'Password does not match'})
        else:
            models.School_system.objects.create(username=username, Email=Email, Password=Password, user_type='admin')
            return render(request, 'SS_signup.html', {'msg':'User has been created successfully'})

@csrf_exempt
def login_controller(request):
    if request.method == 'GET':
        try:
            username = request.session['username']
            user_type = request.session['user_type']
            if request.session['user_type'] == 'admin':
                return redirect('admin_home')
            elif request.session['user_type'] == 'entry':
                return redirect('entry_home')
        except:
            return render(request, 'login_form.html')
    else:
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        try:
            user = models.user.objects.get(Email=Email, Password=Password)
            request.session['username'] = user.username
            request.session['user_type'] = user.user_type
            if request.session['user_type'] == 'admin':
                return redirect('admin_home')
            elif request.session['user_type'] == 'entry':
                return redirect('entry_home')
        except:
            return render(request, 'login_form.html', {'msg':'email or password is incorrect'})

@csrf_exempt
def SS_login_controller(request):
    if request.method == 'GET':
        try:
            username = request.session['username']
            user_type = request.session['user_type']
            if request.session['user_type'] == 'admin':
                return redirect('staff_home')
            elif request.session['user_type'] == 'entry':
                return redirect('student_home')
        except:
            return render(request, 'SS_login.html')
    else:
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        try:
            user = models.School_system.objects.get(Email=Email, Password=Password)
            request.session['username'] = user.username
            request.session['user_type'] = user.user_type
            request.session['userid'] = user.user_id
            try:
                request.session['profile_image'] = user.profile_picture.url
            except:
                pass
            if request.session['user_type'] == 'admin':
                return redirect('staff_home')
            elif request.session['user_type'] == 'entry':
                return redirect('student_home')
        except:
            return render(request, 'SS_login.html', {'msg':'email or password is incorrect'})

@csrf_exempt
def logout_controller(request):
    request.session.flush()
    return redirect('login_route')

def SS_logout_controller(request):
    request.session.flush()
    return redirect('SS_login_route')

@csrf_exempt
def admin_controller(request):
    try:
        username = request.session['username']
        return render(request, 'admin_controller.html')
    except:
        return redirect('login_route')

@csrf_exempt
def staff_controller(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user_id = request.session.get('userid')
        profile_image = request.session.get('profile_image')
        return render(request, 'staff_hp.html', {'username':username, 'userid':user_id, 'profile_image':profile_image})

@csrf_exempt
def entry_home_controller(request):
    try:
        username = request.session['username']
        return render(request, 'entry_home_controler.html')
    except:
        return redirect('login_route')

@csrf_exempt
def student_home_controller(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user_id = request.session.get('userid')
        profile_image = request.session.get('profile_image')
        return render(request, 'studennt_hp.html', {'username':username, 'userid':user_id, 'profile_image':profile_image})

@csrf_exempt
def delete_controller(request,id=None):
    employee_data = models.employee.objects.all()
    emp_obj = models.employee.objects.get(employee_id=id)
    emp_obj.delete()
    return render(request, 'update_controller.html',{'msg': employee_data})

@csrf_exempt
def delete_std_controller(request,id=None):
    std_data = models.student.objects.all()
    std_obj = models.student.objects.get(student_id=id)
    std_obj.delete()
    return render(request, 'std_update_delete_page.html',{'msg': std_data})

@csrf_exempt
def delete_t_controller(request,id=None):
    t_data = models.teachers.objects.all()
    t_obj = models.teachers.objects.get(teacher_id=id)
    t_obj.delete()
    return render(request, 't_update_del.html',{'msg': t_data})

@csrf_exempt
def delete_class_controller(request,id=None):
    c_data = models.Class.objects.all()
    c_obj = models.Class.objects.get(class_id=id)
    c_obj.delete()
    return render(request, 'delete_class.html',{'msg': c_data})

@csrf_exempt
def delete_subject_controller(request,id=None):
    s_data = models.Subject.objects.all()
    s_obj = models.Subject.objects.get(subject_id=id)
    s_obj.delete()
    return render(request, 'up_dell.html',{'msg': s_data})

@csrf_exempt
def add_dicipline(request):
    if request.method == 'GET':
        return render(request, 'Dicipline_data.html')
    else:
        dicipline_name = request.POST.get('dicipline_name')
        msge = discipline.objects.create(discipline_name=dicipline_name)
        message = f"Degree has been stored as : {msge.discipline_name}"
        return render(request, 'Dicipline_data.html', {'msge':message})

@csrf_exempt
def add_emp(request):
    if request.method == 'GET':
        return render(request, 'employee_first.html')
    else:
        empploy_name = request.POST.get('employee_name')
        empploy_age = request.POST.get('employee_age')
        empploy_department = request.POST.get('employee_depart')
        emp = employee.objects.create(employee_name=empploy_name)
        message = f"Data of {emp.employee_name} has been stored successfully"
        return render(request, 'employee_first.html', {'emp':message})

@csrf_exempt
def add_std(request):
    if request.method == 'GET':
        return render(request, 'student_sheet.html')
    else:
        std_name = request.POST.get('std_name')
        std_gender = request.POST.get('std_gender')
        stud_n = student.objects.create(student_name=std_name, student_gender=std_gender)
        message = f"Data of {stud_n.student_name} has been stored successfully"
        return render(request, 'student_sheet.html', {'emp':message})

@csrf_exempt
def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')
    else:
        class_name = request.POST.get('std_class')
        class_obj = Class.objects.create(class_name=class_name)
        message = f"Data of {class_obj.class_name} has been stored successfully"
        return render(request, 'add_class.html', {'emp':message})

@csrf_exempt
def add_sub(request):
    if request.method == 'GET':
        return render(request, 'add_subject.html')
    else:
        sub_name = request.POST.get('sub_name')
        a_obj = Subject.objects.create(subject_name=sub_name)
        message = f"Data of {a_obj.subject_name} has been stored successfully"
        return render(request, 'add_subject.html', {'emp':message})

@csrf_exempt
def add_teach(request):
    if request.method == 'GET':
        return render(request, 'teacher_data.html')
    else:
        t_name = request.POST.get('t_name')
        t_gender = request.POST.get('t_gender')
        t_n = teachers.objects.create(teacher_name=t_name, teacher_gender=t_gender)
        message = f"Data of {t_n.teacher_name} has been stored successfully"
        return render(request, 'teacher_data.html', {'emp':message})

@csrf_exempt
def all_std_data_controller(request):
    if request.method == 'GET':
        all_std_data = models.student.objects.all()
        return render(request, 'view_all_students.html',{'all_std_data':all_std_data})

@csrf_exempt
def all_class_data_controller(request):
    if request.method == 'GET':
        all_class_data = models.Class.objects.all()
        return render(request, 'student_class.html',{'all_class_data':all_class_data})

@csrf_exempt
def all_subject_data_controller(request):
    if request.method == 'GET':
        all_sub_data = models.Subject.objects.all()
        return render(request, 'all_subs.html',{'all_sub_data':all_sub_data})

@csrf_exempt
def teach_data_controller(request):
    if request.method == 'GET':
        all_t_data = models.teachers.objects.all()
        return render(request, 'al_teacher.html',{'all_t_data':all_t_data})

@csrf_exempt
def all_name_data_controller(request):
    if request.method == 'GET':
        all_emp_data = models.employee.objects.all()
        return render(request, 'second.html',{'all_emp_data':all_emp_data})

@csrf_exempt
def all_deg_data_controller(request):
    if request.method == 'GET':
        all_emp_deg_data = models.degree.objects.all()
        return render(request, 'degree_data.html',{'all_emp_deg_data':all_emp_deg_data})

@csrf_exempt
def all_des_data_controller(request):
    if request.method == 'GET':
        all_emp_des_data = models.discipline.objects.all()
        return render(request, 'Dicipline_data.html',{'all_emp_des_data':all_emp_des_data})

def view_all_emp_controller(request):
    employee = models.employee.objects.all()
    return render(request, 'view_employee_name.html',{'all_emp':employee})

def upload_image_controller(request,id):
    if request.method == "POST":
        user = models.School_system.objects.get(user_id=id)
        profile_image = request.FILES.get('img')
        if profile_image:
            user.profile_picture = profile_image
            user.save()
            if request.session['user_type'] == 'admin':
                return redirect('staff_home')
            elif request.session['user_type'] == 'entry':
                return redirect('student_home')

def std_class_combineed(request):
    if request.method == 'GET':
        student_data = models.student.objects.all()
        class_data = models.Class.objects.all()
        return render(request,'std_class_combined.html',{'student':student_data, 'class':class_data})
    else:
        std_id = request.POST.get('std')
        cl_id = request.POST.get('class')
        models.std_class.objects.create(student_id=std_id,Class_id=cl_id)

        student_data = models.student.objects.all()
        class_data = models.Class.objects.all()

        return render(request,'std_class_combined.html',{'message': 'Data has been stored', 'student':student_data, 'class':class_data})

@csrf_exempt
def std_class_update(request):
        SC_Combine = models.std_class.objects.all()
        Class_data = models.Class.objects.all()
        Std_data = models.student.objects.all()
        if request.method == 'GET':
            return render(request, 'SC_update.html', {'C_data':SC_Combine, 'class_data': Class_data, 'Std_data':Std_data})

@csrf_exempt
def std_class_update2(request,an_id):
    SC_Combine = models.std_class.objects.all()
    Class_data = models.Class.objects.all()
    Std_data = models.student.objects.all()
    combine_obj = models.std_class.objects.get(main_id=an_id)
    new_std = request.POST.get('std')
    new_class = request.POST.get('class')

    combine_obj.student_id = new_std
    combine_obj.class_id = new_class

    combine_obj.save()
    return render(request, 'SC_update.html', {'msg':'updated', 'C_data': SC_Combine, 'class_data': Class_data, 'Std_data': Std_data})