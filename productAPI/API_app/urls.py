from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ListCreateProductID.as_view(), name='ProductID'),
    url(r'^$', views.ListCreateProductVar.as_view(), name='ProductVar'),

]