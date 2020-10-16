# Generated by Django 3.0.2 on 2020-10-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20201005_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alt_category',
            field=models.TextField(blank=True, choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('binary search', 'Binary Search'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashsets', 'Hashsets')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('binary search', 'Binary Search'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashsets', 'Hashsets')], default='arrays'),
        ),
    ]
