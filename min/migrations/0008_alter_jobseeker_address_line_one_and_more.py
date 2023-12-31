# Generated by Django 4.2.5 on 2023-10-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('min', '0007_alter_jobseeker_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='address_line_one',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='address_line_two',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='country',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='last_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]
