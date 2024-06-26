# Generated by Django 4.2 on 2024-05-25 15:15

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mysite.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dni",
                    models.CharField(
                        blank=True,
                        max_length=13,
                        null=True,
                        unique=True,
                        verbose_name="Dni",
                    ),
                ),
                ("first_name", models.CharField(max_length=50, verbose_name="Nombres")),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Apellidos"),
                ),
                (
                    "address",
                    models.TextField(blank=True, null=True, verbose_name="Dirección"),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Femenino")],
                        default="M",
                        max_length=1,
                        verbose_name="Sexo",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha Nacimiento"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Telefono"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Correo"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="products/default.png",
                        null=True,
                        upload_to="customers/",
                        verbose_name="Foto",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("state", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
                "ordering": ["last_name"],
            },
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "issue_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Fecha Emision"
                    ),
                ),
                (
                    "subtotal",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=16,
                        verbose_name="Subtotal",
                    ),
                ),
                (
                    "iva",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=16, verbose_name="Iva"
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=16,
                        verbose_name="descuento",
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=16, verbose_name="Total"
                    ),
                ),
                (
                    "payment",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=16, verbose_name="Pago"
                    ),
                ),
                (
                    "change",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=16,
                        verbose_name="Cambio",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("F", "Factura"),
                            ("A", "Anulada"),
                            ("D", "Devolucion"),
                        ],
                        default="F",
                        max_length=1,
                        verbose_name="Estado",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("state", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="customer_invoices",
                        to="core.customer",
                        verbose_name="Cliente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Factura",
                "verbose_name_plural": "Facturas",
                "ordering": ("-issue_date", "customer"),
            },
        ),
        migrations.AddField(
            model_name="product",
            name="cost",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.0"),
                max_digits=10,
                verbose_name="Costo Producto",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="iva",
            field=models.IntegerField(
                choices=[(0, "0%"), (5, "5%"), (15, "15%")],
                default=15,
                verbose_name="IVA",
            ),
        ),
        migrations.AlterField(
            model_name="brand",
            name="state",
            field=models.BooleanField(default=True, verbose_name="Activo"),
        ),
        migrations.AlterField(
            model_name="category",
            name="state",
            field=models.BooleanField(default=True, verbose_name="Activo"),
        ),
        migrations.AlterField(
            model_name="product",
            name="state",
            field=models.BooleanField(default=True, verbose_name="Activo"),
        ),
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.IntegerField(
                default=100,
                help_text="Stock debe estar en 0 y 10000 unidades",
                verbose_name="Stock",
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="phone",
            field=models.CharField(
                max_length=20,
                validators=[
                    django.core.validators.RegexValidator(
                        message="El número de teléfono debe contener entre 9 y 15 dígitos.",
                        regex="^\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="ruc",
            field=models.CharField(
                max_length=13, validators=[mysite.utils.valida_cedula]
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="state",
            field=models.BooleanField(default=True, verbose_name="Activo"),
        ),
        migrations.CreateModel(
            name="PaymentMethod",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Metodo Pago"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("state", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Metodo de Pago",
                "verbose_name_plural": "Metodo de Pagos",
                "ordering": ["description"],
            },
        ),
        migrations.CreateModel(
            name="InvoiceDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=16,
                        null=True,
                    ),
                ),
                (
                    "quantity",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=16),
                ),
                (
                    "subtotal",
                    models.DecimalField(decimal_places=2, default=0, max_digits=16),
                ),
                (
                    "iva",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="detail",
                        to="core.invoice",
                        verbose_name="Factura",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Product",
                        to="core.product",
                        verbose_name="Producto",
                    ),
                ),
            ],
            options={
                "verbose_name": "Factura Detalle",
                "verbose_name_plural": "Factura Detalles",
                "ordering": ("id",),
            },
        ),
        migrations.AddField(
            model_name="invoice",
            name="payment_method",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="payment_invoices",
                to="core.paymentmethod",
                verbose_name="Metodo pago",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddIndex(
            model_name="invoicedetail",
            index=models.Index(fields=["id"], name="core_invoic_id_045dfe_idx"),
        ),
        migrations.AddIndex(
            model_name="invoice",
            index=models.Index(
                fields=["issue_date"], name="core_invoic_issue_d_99a2a6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="invoice",
            index=models.Index(
                fields=["customer"], name="core_invoic_custome_2bcf11_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="customer",
            index=models.Index(
                fields=["last_name"], name="core_custom_last_na_c56f78_idx"
            ),
        ),
    ]
