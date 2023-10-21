# Generated by Django 4.2.5 on 2023-10-11 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('min', '0005_alter_jobseeker_code_alter_jobseeker_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='code',
            field=models.CharField(choices=[('+91', '+91'), ('+1', '+1')], max_length=3),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='experience',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5+', '5+')], max_length=2),
        ),
    ]