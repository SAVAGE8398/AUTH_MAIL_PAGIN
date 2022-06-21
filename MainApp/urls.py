from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('crm/',views.crm,name='crm'),
    path('crm/delete/',views.delete),
    path('crm/edit/',views.edit),
    path('crm/edit/update',views.update),
    path('logout',views.logout,name='logout'),
]
