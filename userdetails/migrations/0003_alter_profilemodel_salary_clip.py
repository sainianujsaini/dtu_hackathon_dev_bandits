# Generated by Django 4.0.4 on 2022-05-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0002_delete_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='Salary_clip',
            field=models.FileField(upload_to='images/userprofile/salarslips'),
        ),
    ]
