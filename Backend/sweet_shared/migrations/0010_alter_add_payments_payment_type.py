# Generated by Django 3.2.7 on 2025-01-23 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_shared', '0009_alter_add_payments_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_payments',
            name='payment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_types_add', to='sweet_shared.bankinformation', verbose_name='نوع الدفع'),
        ),
    ]
