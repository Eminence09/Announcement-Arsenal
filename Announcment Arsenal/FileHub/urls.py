from django.urls import path
from . import views


urlpatterns = [
    path('', views.files, name='file_upload'),
    path('user_data/', views.show_data, name="show_data"),
    path('filesrestored/', views.delete_all_file, name="del_data"),
    # path('file_info/', views.file_info, name="file_information"),
    path('/', views.files, name="files"),
]