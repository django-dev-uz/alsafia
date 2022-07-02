# Generated by Django 3.2.12 on 2022-07-02 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myshop', '0007_rename_cartmodel_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(blank=True, related_name='wishlist', to='myshop.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]