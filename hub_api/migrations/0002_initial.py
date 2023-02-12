# Generated by Django 4.1.5 on 2023-02-12 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mirusers', '0001_initial'),
        ('hub_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mirusers.hub', verbose_name='Shipped from location'),
        ),
        migrations.AddField(
            model_name='order',
            name='updatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updatedBy', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='hub_api.order'),
        ),
    ]