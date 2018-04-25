from django.conf.urls import url
from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    # Class-based views
    path('', ProductLV.as_view(), name='index'),

    # Example : /add/
    path('add/', ProductCreateView.as_view(), name='add'),
    # Example : /99/update/
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    # Example : /99/delete/
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
]
