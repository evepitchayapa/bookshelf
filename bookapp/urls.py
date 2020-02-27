from django.urls import path,include
from . import views

app_name = 'bookapp'
urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('search/',views.search,name='search'),
    #--------------------- login part
    path('accounts/signup/',views.signup,name='signup'),
    path('accounts/signup/createuser',views.createuser,name='createuser'),
    path('logout/',views.logout,name='logout'),
    path ('querybyuser/',views.querybyuser,name='querybyuser')

]