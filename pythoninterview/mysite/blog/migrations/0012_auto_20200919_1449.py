# Generated by Django 3.0.2 on 2020-09-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_alt_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alt_category',
            field=models.TextField(blank=True, choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('trees', 'Trees'), ('graphs', 'Graphs')], null=True),
        ),
    ]