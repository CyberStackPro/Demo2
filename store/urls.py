from django.urls import path
from . import views


urlpatterns = [
    # path('products/', views.product_list, name='product_list'),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('collections/', views.CollectionList.as_view(), name='collection_list'),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(),
         name='collection-detail'),
    # path('', views.product_list, name='product_list'),
    # path('tags/<slug:tag_slug>', views.product_list, name='product_list_by_tag'),
    # path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
]
