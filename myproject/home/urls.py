# myproject/home/urls.py

from django.urls import path
from . import views
from .views import sse_binary_view,sse_binary_example_view


urlpatterns = [
    
    
    path('run_frequency_test/', views.run_frequency_test, name='run_frequency_test'),

]

# http://127.0.0.1:8000/sse_binary_example/