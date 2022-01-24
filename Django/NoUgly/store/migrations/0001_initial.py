# Generated by Django 3.2.8 on 2022-01-24 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('zipcode', models.IntegerField()),
                ('adress', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product_kind',
            fields=[
                ('kind', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('fIDX', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=5)),
                ('date', models.DateTimeField()),
                ('weight', models.IntegerField()),
                ('Field', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product_kind')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('purchase_time', models.DateTimeField()),
                ('fIDX', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('fIDX', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('uIDX', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='회원')),
            ],
        ),
    ]
