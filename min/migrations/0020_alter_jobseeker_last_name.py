# Generated by Django 4.2.5 on 2023-10-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('min', '0019_alter_jobseeker_address_line_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
    ]