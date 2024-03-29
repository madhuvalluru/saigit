# Generated by Django 2.2 on 2019-11-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=250)),
                ('blood_group', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('creates', models.DateField(auto_now_add=True)),
                ('number', models.CharField(max_length=25)),
            ],
        ),
    ]
