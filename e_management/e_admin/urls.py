from django.urls import path
from . import views

urlpatterns=[
    path("employe/add",views.emp_create,name="addemployee"),
    path("employe/view",views.emp_view,name="viewemployee"),
    path("employe/remove/<int:id>",views.emp_remove,name="delemployee"),
    path("employe/update/<int:id>",views.emp_update,name="empupdate"),
    path("employe/detail/<int:id>",views.emp_details,name="empdetails"),

    path("dep/add",views.dep_creation,name="departmentadd"),
    path("dep/view", views.dep_view, name="viewdepartment"),
    path("dep/remove/<int:id>",views.dep_remove,name="deldepu"),
    path("dep/update/<int:id>",views.dep_update,name="depupdation"),
    path("dep/details/<int:id>",views.dep_details,name="depdetails"),

    path("login",views.signin,name="login"),
    path("logout",views.signout,name="logout"),
    path("index",views.admin_index,name="index"),
]