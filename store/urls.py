from django.urls import path, include
# import include
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter
from pprint import pprint
from playground.urls import urlpatterns
from . import views

# router = SimpleRouter()
router = routers.DefaultRouter()

router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('cart', views.CartViewSet, basename='cart')
# pprint(
#     router.urls

# )

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
# urlpatterns = [
#     path('products/', views.product_list, name='product_list'),
#     path('products/', views.ProductList.as_view(), name='product_list'),
#     path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
#     path('collections/', views.CollectionList.as_view(), name='collection_list'),
#     path('collections/<int:pk>/', views.CollectionDetail.as_view(),
#          name='collection-detail'),
#     path('', views.product_list, name='product_list'),
#     path('tags/<slug:tag_slug>', views.product_list, name='product_list_by_tag'),
#     path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
# ]

urlpatterns = [
    # + products_router.urls
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls))
]
