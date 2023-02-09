from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:id>',views.customerDetails,name='details'),
    path('transfer/<str:id>',views.transfer,name='transfer'),
    path('execute',views.execute),
    path('execute/<str:id1>/<str:id2>',views.execute,name='execute')
]