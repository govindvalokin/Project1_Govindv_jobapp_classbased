from django.urls import path
from . import views
# from min import views
from .views import *

urlpatterns = [
    # For Function based views 
    # path('index/',views.index,name="index"),
    # path("",views.index,name="index"),
    # path('newform/',views.newform,name="jobform"),
    # path('addnew',views.addnew,name="addnew"),
    # path('updateform/',views.updateform,name="updateform"),
    # path('deleteform/',views.deleteData,name="delete"),
    
    
    # path('listing/', applicant_List_View.as_view()),
    # path('dform/', create_List_View.as_view()),

    #for class based views
    path('userlistview/', UserListView.as_view(), name="user_data"),
    path('', UserListView.as_view(), name="user_data"),
    path('usercreateview/', UserCreateView.as_view(),name="new_user"),
    path('userupdateview/<int:pk>/', views.UserUpdateView.as_view(), name="update"),
    path('userdeleteview/<int:pk>/', views.UserDeleteView.as_view(), name="delete"),
]