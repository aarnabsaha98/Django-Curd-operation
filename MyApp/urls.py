from django.urls import path
from . import views 

urlpatterns = [
path('detail/<int:id>/' ,views.View , name='detail-view'),
path('curd/' ,views.Create , name='create'),
path('delete/<int:id>/' ,views.delete , name='delete'),
path('update/<int:id>/' ,views.update , name='update'),

]