# Generated by Django 5.0.6 on 2024-06-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='media/images'),
            preserve_default=False,
        ),
    ]