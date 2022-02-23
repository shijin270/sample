from django.conf.urls import url
from temp import views
urlpatterns=[
    url('^admin/',views.admin_home),
    url('^student/',views.student_home),
    url('^login/',views.login),
    url('^add/',views.add),
    url('^stu/',views.stu),

]