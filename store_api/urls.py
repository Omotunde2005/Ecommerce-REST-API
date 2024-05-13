from django.urls import path
from rest_framework.authtoken import views
from store_api.views import (AllProductsView, CreateProductView,
                             EditProductView, GetAllStoresView,
                             GetSingleProductView, GetSingleStoreView, GetUserSales, DeleteProductView)


urlpatterns = [
    path("products/", AllProductsView.as_view(), name="all-products"),
    path("product/create/", CreateProductView.as_view(), name="create-products"),
    path("product/edit/<str:URL>/", EditProductView.as_view(), name="edit-products"),
    path("product/delete/<str:URL>/", DeleteProductView.as_view(), name="delete-product"),
    path("product/<str:URL>/", GetSingleProductView.as_view(), name="single-product"),
    path("stores/", GetAllStoresView.as_view(), name="get-stores"),
    path("store/<int:pk>/", GetSingleStoreView.as_view(), name="single-store"),
    path("store/sales/", GetUserSales.as_view(), name="user-sales"),
    path("auth/", views.obtain_auth_token, name="get-token")
]