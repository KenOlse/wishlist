# Generated by Django 3.2.7 on 2021-09-17 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210915_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistuser',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='main.product'),
        ),
    ]
