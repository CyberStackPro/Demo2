from django.urls import path
from store.views import product_detail
from . import views


urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('collections/<int:pk>/', views.collection_detail,
         name='collection-detail'),
    # path('', views.product_list, name='product_list'),
    # path('tags/<slug:tag_slug>', views.product_list, name='product_list_by_tag'),
    # path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
]
