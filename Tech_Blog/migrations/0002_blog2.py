# Generated by Django 5.0.6 on 2024-07-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_id', models.CharField(max_length=255)),
                ('Blog_title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'blog_Table2',
            },
        ),
    ]
