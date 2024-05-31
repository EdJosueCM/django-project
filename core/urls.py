from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    # Product views urls
    path("product_list/", views.product_List, name="product_list"),
    path("product_create/", views.product_Create, name="product_create"),
    path("product_update/<int:id>/", views.product_Update, name="product_update"),
    path("product_delete/<int:id>/", views.product_Delete, name="product_delete"),
    # Brands views urls
    path("brand_list/", views.brands_List, name="brand_list"),
    path("brand_create/", views.brands_Create, name="brand_create"),
    path("brand_update/<int:id>/", views.brands_Update, name="brand_update"),
    path("brand_delete/<int:id>/", views.brands_Delete, name="brand_delete"),
    # Supplier views urls
    path("supplier_list/", views.supplier_List, name="supplier_list"),
    path("supplier_create/", views.suppliers_Create, name="supplier_create"),
    path("supplier_update/<int:id>/", views.suppliers_Update, name="supplier_update"),
    path("supplier_delete/<int:id>/", views.suppliers_Delete, name="supplier_delete"),
    # Category views urls
    path("category_list/", views.category_list, name="category_list"),
    path("category_create/", views.category_Create, name="category_create"),
    path("category_update/<int:id>/", views.category_Update, name="category_update"),
    path("category_delete/<int:id>/", views.category_Delete, name="category_delete"),
    # Signup
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("signin/", views.signin, name="signin"),
]
