# Generated by Django 4.0.4 on 2022-05-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0006_alter_loanrequestspost_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequestspost',
            name='accepted_user',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]