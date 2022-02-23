from django.db import models

# Create your models here.
class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'student'



class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    u_id = models.IntegerField()
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'login'


class Mark(models.Model):
    m_id = models.AutoField(primary_key=True)
    # s_id = models.IntegerField()
    s=models.ForeignKey(Student,to_field='s_id',on_delete=models.CASCADE)
    assignment = models.IntegerField()
    series_test = models.IntegerField()
    attendance = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mark'
