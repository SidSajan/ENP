# Generated by Django 2.2 on 2019-05-07 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190505_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normallogin',
            name='enp_string',
            field=models.TextField(),
        ),
    ]
