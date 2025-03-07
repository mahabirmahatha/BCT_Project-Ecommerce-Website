# Generated by Django 5.1.6 on 2025-03-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
