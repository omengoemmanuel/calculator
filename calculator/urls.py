from django.urls import path
from . import views

urlpatterns = [
    path('', views.cal1, name='cal1'),
    path('function', views.function, name = 'function'),
    path('investment', views.investment, name='investment'),
    path('invest_sub', views.invest_sub, name='invest_sub')

]
