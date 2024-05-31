from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from core.models import Product, Brand, Supplier, Category
from core.forms import ProductForm, BrandForm, SupplierForm, CategoryForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import re

# Create your views here.
def home(request):
    data = {"title1": "FUTI", "title2": "Super Mercado Economico"}

    return render(request, "core/home.html", data)


def is_password_strong(password):
    # Verificar longitud mínima
    if len(password) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    
    # Verificar que contenga al menos una letra
    if not re.search(r"[a-zA-Z]", password):
        return False, "La contraseña debe contener al menos una letra."
    
    # Verificar que contenga al menos un número
    if not re.search(r"\d", password):
        return False, "La contraseña debe contener al menos un número."
    
    # Verificar que contenga al menos un símbolo
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>-_]", password):
        return False, "La contraseña debe contener al menos un símbolo."
    
    return True, ""

def signup(request):
    if request.method == "GET":
        return render(request, "core/signup/signup.html", {"form": UserCreationForm()})
    else:
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            return render(
                request,
                "core/signup/signup.html",
                {"form": UserCreationForm(), "error": "Las contraseñas no coinciden."},
            )

        if password1 == username:
            return render(
                request,
                "core/signup/signup.html",
                {"form": UserCreationForm(), "error": "La contraseña no puede ser igual al nombre de usuario."},
            )

        is_strong, message = is_password_strong(password1)
        if not is_strong:
            return render(
                request,
                "core/signup/signup.html",
                {"form": UserCreationForm(), "error": message},
            )

        try:
            user = User.objects.create_user(
                username=username,
                password=password1,
            )
            user.save()
            login(request, user)
            return redirect("home")
        except IntegrityError:
            return render(
                request,
                "core/signup/signup.html",
                {"form": UserCreationForm(), "error": "El usuario ya existe."},
            )


def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "core/signin/signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(request, "core/signin/signin.html", 
                          {"form": AuthenticationForm,
                           'error': 'Usuario o contraseña es incorrecta.'
                           })
        else:
            login(request, user)
            return redirect('home')


# Product Views
def product_List(request):
    data = {"title1": "Products", "title2": "Consulta de Productos"}

    products = Product.objects.all()
    data["products"] = products

    return render(request, "core/products/list.html", data)


# Create Product
@login_required
def product_Create(request):
    data = {"title1": "Productos", "title2": "Ingreso de Productos"}

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("core:product_list")
        else:
            data["form"] = form  # Pasar el formulario con errores
    else:
        data["form"] = ProductForm()  # Formulario sin datos

    return render(request, "core/products/form.html", data)


# Update Product
@login_required
def product_Update(request, id):
    data = {"title1": "Productos", "title2": ">Edicion De Productos"}
    product = Product.objects.get(pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("core:product_list")
    else:
        form = ProductForm(instance=product)
        data["form"] = form
    return render(request, "core/products/form.html", data)


# Delete Product
@login_required
def product_Delete(request, id):
    product = Product.objects.get(pk=id)
    data = {"title1": "Eliminar", "title2": "Eliminar Un Producto", "product": product}
    if request.method == "POST":
        product.delete()
        return redirect("core:product_list")

    return render(request, "core/products/delete.html", data)


# Brands Views
def brands_List(request):
    data = {"title1": "Brands", "title2": "Consulta de Marcas"}

    brands = Brand.objects.all()
    data["brands"] = brands
    return render(request, "core/brands/list.html", data)


# Brands Create
@login_required
def brands_Create(request):
    data = {"title1": "Marcas", "title2": "Crear Marcas"}

    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
            brand.save()
            return redirect("core:brand_list")

    else:
        data["form"] = BrandForm()  # controles formulario sin datos

    return render(request, "core/brands/form.html", data)


# Brands Update
@login_required
def brands_Update(request, id):
    data = {"title1": "Marcas", "title2": "Edicion De Marcas"}
    brand = Brand.objects.get(pk=id)
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect("core:brand_list")
    else:
        form = BrandForm(instance=brand)
        data["form"] = form
    return render(request, "core/brands/form.html", data)


# Brands Delete
@login_required
def brands_Delete(request, id):
    brand = Brand.objects.get(pk=id)
    data = {"title1": "Eliminar", "title2": "Eliminar Un Producto", "brand": brand}
    if request.method == "POST":
        brand.delete()
        return redirect("core:brand_list")

    return render(request, "core/brands/delete.html", data)


# Supplier Views
def supplier_List(request):
    data = {"title1": "Suppliers", "title2": "Consulta de proveedores"}

    suppliers = Supplier.objects.all()
    data["suppliers"] = suppliers
    return render(request, "core/suppliers/list.html", data)


# Suppliers Create
@login_required
def suppliers_Create(request):
    data = {"title1": "Proveedores", "title2": "Crear Proveedores"}

    if request.method == "POST":
        try:
            form = SupplierForm(request.POST, request.FILES)
            if form.is_valid():
                brand = form.save(commit=False)
                brand.user = request.user
                brand.save()
                return redirect("core:supplier_list")
            
        except:
            data['form'] = form
            return render(request, 'core/suppliers/form.html', data)
    else:
        data["form"] = SupplierForm()  # controles formulario sin datos

    return render(request, "core/suppliers/form.html", data)


# Suppliers Update
@login_required
def suppliers_Update(request, id):
    data = {"title1": "Proveedor", "title2": "Edicion De Proveedores"}
    supplier = Supplier.objects.get(pk=id)
    if request.method == "POST":
        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect("core:supplier_list")
    else:
        form = SupplierForm(instance=supplier)
        data["form"] = form
    return render(request, "core/suppliers/form.html", data)

@login_required
def suppliers_Delete(request, id):
    supplier = Supplier.objects.get(pk=id)
    data = {
        "title": "Eliminar",
        "title2": "Eliminar un Proveedor",
        "supplier": supplier,
    }
    if request.method == "POST":
        supplier.delete()
        return redirect("core:supplier_list")

    return render(request, "core/suppliers/delete.html", data)


# Category View
def category_list(request):
    data = {"title1": "Category", "title2": "Consulta de Categorias"}
    category = Category.objects.all()
    data["category"] = category
    return render(request, "core/category/list.html", data)

@login_required
def category_Create(request):
    data = {"title1": "Categorias", "title2": "Crear Categorias"}
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("core:category_list")
    else:
        data["form"] = CategoryForm()

    return render(request, "core/category/form.html", data)

@login_required
def category_Update(request, id):
    data = {"title1": "Categorias", "title2": "Edicion de Categorias"}
    category = Category.objects.get(pk=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect("core:category_list")
    else:
        form = CategoryForm(instance=category)
        data["form"] = form
    return render(request, "core/category/form.html", data)

@login_required
def category_Delete(request, id):
    category = Category.objects.get(pk=id)
    data = {
        "title1": "Eliminar",
        "title2": "Eliminar una Categoria",
        "category": category,
    }
    if request.method == "POST":
        category.delete()
        return redirect("core:category_list")

    return render(request, "core/category/delete.html", data)
