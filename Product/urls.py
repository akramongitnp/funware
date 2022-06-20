from django.urls import path
from . import views

urlpatterns = [
    path('requested_product', views.requested_product, name='requested_products'),
    path('feedpost', views.feedpost, name='feedpost'),

]

