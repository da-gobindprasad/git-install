from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='product_list'),
    # path('', views.IndexClassView.as_view(), name='product_list'),
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # product list
    path('<int:pk>', views.ProductDetail.as_view(), name='details'),
    path('update/<int:id>/', views.update_item, name='update'),


]
