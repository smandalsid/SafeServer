# Generated by Django 4.1.7 on 2023-03-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptostego', '0002_remove_image_id_alter_image_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
