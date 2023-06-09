# Generated by Django 4.2.1 on 2023-06-04 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_remove_orders_cart_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
