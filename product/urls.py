from django.urls import path, include,re_path

from .views import index,ProductsListView,detailproduct,grouping,gproduct,add_cart,cart,delete_cart
name_app='product'

urlpatterns = [
    path('', index,name ='index'),
    path('products/', ProductsListView.as_view(),name ='products'),
    path('detail/<int:id>/',detailproduct,name ='productsd'),
    path('grouping/',grouping,name ='group'),
    path('gproduct/<int:id>/',gproduct,name ='gproduct'),
    path('buy/<int:id>/',add_cart,name ='buy'),
    path('cart/',cart,name ='cart'),
    path('delete/<int:id>/',delete_cart,name ='delete'),
    
]
