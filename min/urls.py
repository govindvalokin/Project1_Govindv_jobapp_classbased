from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # for class based views
    path("userlistview/", UserListView.as_view(), name="user_data"),
    path("", UserListView.as_view(), name="user_data"),
    path("usercreateview/", UserCreateView.as_view(), name="new_user"),
    path("userupdateview/<int:pk>/", views.UserUpdateView.as_view(), name="update"),
    path("userdeleteview/<int:pk>/", views.UserDeleteView.as_view(), name="delete"),
    path("searchlist/", views.SearchList.as_view(), name="searchlist"),
]
