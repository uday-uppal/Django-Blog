# Generated by Django 4.0.2 on 2022-02-15 17:45

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogmodel_author_blogmodel_read_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000)),
                ('message', froala_editor.fields.FroalaField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
