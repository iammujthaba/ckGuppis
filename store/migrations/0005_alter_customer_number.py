# Generated by Django 5.0.6 on 2024-06-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='number',
            field=models.CharField(max_length=12),
        ),
    ]