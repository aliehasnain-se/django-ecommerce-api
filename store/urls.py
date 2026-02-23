from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.CollectionListCreateApi.as_view()),
    path('collections/<int:pk>/', views.CollectionRetrieveUpdateDestroyAPI.as_view()),

    path('products/', views.ProductListCreateApi.as_view()),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPI.as_view()),
    
    path('products/<int:product_pk>/reviews/', views.ReviewListCreateApi.as_view()),
    path('products/<int:product_pk>/reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPI.as_view()),

    path('products/<int:product_pk>/images/', views.ProductImageListCreateAPIView.as_view()),
    path('products/<int:product_pk>/images/<int:pk>/', views.ProductImageRetrieveUpdateDestroyAPIView.as_view()),

    path('carts/', views.CartCreateApi.as_view()),
    path('carts/<uuid:cart_pk>/', views.CartRetrieveDestroyAPI.as_view()),
    path('carts/<uuid:cart_pk>/items/', views.CartItemListCreateApi.as_view()),
    path('carts/<uuid:cart_pk>/items/<int:pk>/', views.CartItemRetrieveUpdateDestroyAPI.as_view()),

    path('customers/', views.CustomerCreateAPIView.as_view()),
    path('customers/me/', views.CurrentCustomerRetrieveUpdateAPIView.as_view()),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateAPIView.as_view()),
    
    path('orders/', views.OrderApiView.as_view()),

]