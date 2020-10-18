# Generated by Django 3.0.2 on 2020-09-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200917_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('trees', 'Trees'), ('graphs', 'Graphs')], default='arrays'),
        ),
        migrations.AlterField(
            model_name='post',
            name='difficulty',
            field=models.TextField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy'),
        ),
    ]