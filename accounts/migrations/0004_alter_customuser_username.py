# Generated by Django 4.0.4 on 2022-05-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.EmailField(default='', max_length=10, unique=True),
        ),
    ]