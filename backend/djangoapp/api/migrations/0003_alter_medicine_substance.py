# Generated by Django 5.1.1 on 2024-09-26 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_medicine_laboratory_alter_medicine_substance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='substance',
            field=models.TextField(),
        ),
    ]
