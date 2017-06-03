from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^product/$', views.ListCreateProduct.as_view(), name='Product'),
    url(r'^productvar/$', views.ListCreateProductVar.as_view(), name='ProductVar'),
    url(r'^category/$', views.ListCreateCategory.as_view(), name='Category'),
]