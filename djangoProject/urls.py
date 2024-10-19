"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('second',views.all_name_data_controller),
    path('add_emp',views.add_emp),
    path('add_deg',views.add_deg),
    path('add_des',views.add_dicipline),
    path('class',views.add_class),
    path('subject',views.add_sub),
    path('all_employee_data',views.all_name_data_controller),
    path('all_subject',views.all_subject_data_controller),
    path('class_data',views.all_class_data_controller),
    path('all_employee_deg',views.all_deg_data_controller),
    path('all_employee_des',views.all_des_data_controller),
    path('view_employee',views.view_all_emp_controller),
    path('update',views.update_controller),
    path('std_update',views.update_std_controller),
    path('t_update',views.update_t_controller),
    path('c_update',views.update_class_controller),
    path('s_update',views.update_subject_controller),
    path('std_update/<id>',views.update_std_controller),
    path('t_update/<id>',views.update_t_controller),
    path('c_update/<id>',views.update_class_controller),
    path('s_update/<id>',views.update_subject_controller),
    path('update/<id>',views.update_controller),
    path('delete/<id>',views.delete_controller),
    path('t_delete/<id>',views.delete_t_controller),
    path('c_delete/<id>',views.delete_class_controller),
    path('s_delete/<id>',views.delete_subject_controller),
    path('std_delete/<id>',views.delete_std_controller),
    path('upload_img/<int:id>',views.upload_image_controller),
    path('signup',views.sigup_controller),
    path('SS_signup',views.SS_sigup_controller),
    path('login',views.login_controller,name='login_route'),
    path('SS_login',views.SS_login_controller,name='SS_login_route'),
    path('admin',views.admin_controller, name='admin_home'),
    path('staff',views.staff_controller, name='staff_home'),
    path('entry_home',views.entry_home_controller, name='entry_home'),
    path('std_home',views.student_home_controller, name='student_home'),
    path('logout',views.logout_controller),
    path('SS_logout',views.SS_logout_controller),
    path('student',views.add_std),
    path('teacher',views.add_teach),
    path('all_student',views.all_std_data_controller),
    path('all_teacher',views.teach_data_controller),
    path('add_SC',views.std_class_combineed),
    path('all_SC_update',views.std_class_update),
    path('all_SC_update2/<an_id>',views.std_class_update2)

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)