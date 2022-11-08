from.import views
from django.urls import path
app_name='timetableapp'
urlpatterns=[
    path('', views.add, name='add'),
   path('detail/', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='update'),
   path('delete/<int:id>', views.delete, name='delete'),
    path('cbhome',views.Timetablelistview.as_view(), name='cbhome'),
   path('cbdetail/<int:pk>/',views.Timetabledetailview.as_view(), name='cbdetail'),
    path('cbupdate/<int:pk>/',views.Timetableupdateview.as_view(), name='cbupdate'),
   path('cbdelete/<int:pk>/',views.Timetabledeleteview.as_view(), name='cbdelete')
]