# app urls


from django.urls import path
from myapp import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('delete-emp/<int:emp_id>/',views.delete ,name='delete'),

]