# Generated by Django 3.0.2 on 2020-11-24 02:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('title', ckeditor.fields.RichTextField()),
                ('category', models.TextField(choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('binary search', 'Binary Search'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('recursion', 'Recursion'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashsets', 'Hashsets')], default='arrays')),
                ('alt_category', models.TextField(blank=True, choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('binary search', 'Binary Search'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('recursion', 'Recursion'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashsets', 'Hashsets')], null=True)),
                ('difficulty', models.TextField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy')),
                ('description', ckeditor.fields.RichTextField()),
                ('text', ckeditor.fields.RichTextField()),
                ('explanation', ckeditor.fields.RichTextField()),
                ('additional_notes', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
