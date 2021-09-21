# Generated by Django 3.2.3 on 2021-05-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
