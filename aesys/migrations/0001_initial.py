# Generated by Django 4.0.3 on 2022-07-05 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=80)),
                ('contact_no', models.CharField(max_length=11)),
                ('customer_email', models.EmailField(max_length=80)),
                ('City_or_Municipality', models.CharField(max_length=200)),
                ('Province', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concern_type', models.CharField(choices=[('R', 'Reques'), ('Q', 'Question'), ('C', 'Complaints'), ('O', 'Others')], max_length=100, null=True)),
                ('message', models.TextField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aesys.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=999)),
                ('quantity', models.PositiveIntegerField()),
                ('order_date', models.DateField(auto_now_add=True)),
                ('delivery_type', models.CharField(choices=[('SD', 'Same Day Delivery'), ('ND', 'Normal Delivery')], max_length=100, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aesys.customer')),
            ],
        ),
    ]
