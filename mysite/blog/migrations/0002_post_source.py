# Generated by Django 3.2.16 on 2023-01-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]
