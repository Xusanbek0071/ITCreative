# Generated by Django 4.2.4 on 2023-09-09 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
