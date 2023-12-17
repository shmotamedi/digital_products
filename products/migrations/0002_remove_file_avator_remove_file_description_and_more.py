# Generated by Django 4.1.12 on 2023-12-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="avator",
        ),
        migrations.RemoveField(
            model_name="file",
            name="description",
        ),
        migrations.AddField(
            model_name="file",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="Products"),
        ),
        migrations.AddField(
            model_name="file",
            name="file",
            field=models.FileField(default=3, upload_to="files/%Y/%m/%d"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="file",
            name="product",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="categories",
            field=models.ManyToManyField(blank=True, to="products.category"),
        ),
        migrations.AlterField(
            model_name="category",
            name="avator",
            field=models.ImageField(blank=True, upload_to="Categories/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="avator",
            field=models.ImageField(blank=True, upload_to="Products/"),
        ),
    ]