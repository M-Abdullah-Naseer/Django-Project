from django.db import models

# Create your models here.
# Create your models here.
class employee(models.Model):
    employee_id = models.AutoField(primary_key= True)
    employee_name = models.CharField(max_length=100)

class Class(models.Model):
    class_id = models.AutoField(primary_key= True)
    class_name = models.CharField(max_length=100)

class Subject(models.Model):
    subject_id = models.AutoField(primary_key= True)
    subject_name = models.CharField(max_length=100)

class student(models.Model):
    student_id = models.AutoField(primary_key= True)
    student_name = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=100)

class teachers(models.Model):
    teacher_id = models.AutoField(primary_key= True)
    teacher_name = models.CharField(max_length=100)
    teacher_gender = models.CharField(max_length=100)

class user(models.Model):
    user_id = models.AutoField(primary_key= True)
    username = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_picture/')

class School_system(models.Model):
    user_id = models.AutoField(primary_key= True)
    username = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_picture/')

class degree(models.Model):
    degree_id = models.AutoField(primary_key= True)
    degree_name = models.CharField(max_length=100)

class discipline(models.Model):
    discipline_id = models.AutoField(primary_key= True)
    discipline_name = models.CharField(max_length=100)

class employee_qualification(models.Model):
    employee_qualification_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    degree = models.ForeignKey(degree, on_delete=models.CASCADE)
    discipline = models.ForeignKey(discipline, on_delete=models.CASCADE)
    total_makrs = models.IntegerField()
    marks_obtained = models.IntegerField()
    passing_year = models.IntegerField()

class std_class(models.Model):
    main_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)

class relation(models.Model):
    relation_id = models.AutoField(primary_key= True)
    relation_name = models.CharField(max_length=100)
class Employee_family_members(models.Model):
    emp_fam_mem_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    relation = models.ForeignKey(relation, on_delete=models.CASCADE)
    fam_mem_name_name = models.CharField(max_length=100)
    fam_mem_dob = models.DateField()
    fam_mem_gender = models.CharField(max_length=30)
    fam_mem_cnic = models.IntegerField()
    fam_mem_living_status = models.CharField(max_length=6)

class country(models.Model):
    country_id = models.AutoField(primary_key= True)
    country_name = models.CharField(max_length=100)
class city(models.Model):
    city_id = models.AutoField(primary_key= True)
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)