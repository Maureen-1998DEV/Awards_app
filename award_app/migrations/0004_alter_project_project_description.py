# Generated by Django 3.2.8 on 2021-10-25 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0003_rename_profile_pic_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.CharField(max_length=3000),
        ),
    ]