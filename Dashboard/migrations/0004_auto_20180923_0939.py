# Generated by Django 2.1.1 on 2018-09-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_course_course_logo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_logo_url',
            field=models.CharField(max_length=1000),
        ),
    ]
