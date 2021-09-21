# Generated by Django 2.2.20 on 2021-09-21 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('userpic', models.ImageField(default='0', upload_to='user_details')),
                ('email', models.EmailField(default='0', max_length=254)),
                ('mbno', models.CharField(default='0', max_length=15)),
                ('adhaarno', models.CharField(default='0', max_length=17)),
                ('city', models.CharField(default='beawar', max_length=50)),
                ('fadhaar', models.ImageField(default='0', upload_to='user_details')),
                ('badhaar', models.ImageField(default='0', upload_to='user_details')),
                ('pwd', models.CharField(max_length=20)),
                ('gender', models.CharField(default=0, max_length=11)),
            ],
        ),
    ]
