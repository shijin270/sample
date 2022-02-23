from django.conf.urls import url
from student import views
urlpatterns=[
    url('^Student_registration/',views.student_registration),
    url('^Admin/',views.admin),
    url('^View_student/',views.view_student),
    url('^Add_mark/',views.add_mark),
    url('^View_mark/',views.view_mark),
    url('^update/',views.update),
    url('edit_mark/(?P<idd>\w+)', views.edit_mark, name='edit_mark'),
]