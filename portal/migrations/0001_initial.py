# Generated by Django 2.2.20 on 2021-09-21 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('minamnt', models.IntegerField(default=0)),
                ('date', models.DateField(verbose_name='date')),
                ('description', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=15)),
                ('document', models.ImageField(upload_to='property_details')),
                ('pic1', models.ImageField(upload_to='property_details')),
                ('pic2', models.ImageField(upload_to='property_details')),
                ('pic3', models.ImageField(upload_to='property_details')),
                ('pic4', models.ImageField(upload_to='property_details')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.credentials')),
            ],
        ),
    ]