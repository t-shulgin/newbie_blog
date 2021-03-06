# Generated by Django 3.1.2 on 2020-10-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50)),
                ('blog_date', models.CharField(max_length=20)),
                ('blog_text', models.CharField(max_length=1500)),
                ('blog_image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]
