


#app_name = 'backend'
#urlpatterns = [
  #  #path('', views.api_home, name='api_home'),
#]

from django.urls import path, include
from backend import views

urlpatterns = [
  path('bodega-api/', views.metauser_list),
]