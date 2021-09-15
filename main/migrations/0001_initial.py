# Generated by Django 3.2.7 on 2021-09-14 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Продукт')),
                ('link', models.URLField(help_text='Укажіть інтернет адресу', verbose_name='Інтернет-адреса')),
                ('price', models.IntegerField(help_text='Укажіть ціну', verbose_name='Ціна продукту')),
                ('added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Додано')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
            },
        ),
        migrations.CreateModel(
            name='WishListUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('is_hidden', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='main.product')),
                ('product_user', models.ManyToManyField(related_name='product', to='main.Product')),
            ],
        ),
    ]
