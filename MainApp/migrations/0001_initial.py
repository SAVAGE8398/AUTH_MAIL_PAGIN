# Generated by Django 4.0.3 on 2022-06-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameF', models.CharField(max_length=255)),
                ('EmailF', models.CharField(max_length=255)),
                ('PasswordF', models.CharField(max_length=255)),
            ],
        ),
    ]