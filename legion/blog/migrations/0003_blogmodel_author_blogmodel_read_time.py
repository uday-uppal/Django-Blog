# Generated by Django 4.0.2 on 2022-02-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='author',
            field=models.CharField(default='Uday Uppal', max_length=1000),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='read_time',
            field=models.IntegerField(default=5),
        ),
    ]
