# Generated by Django 3.0.2 on 2020-11-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alt_category',
            field=models.TextField(blank=True, choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('binary search', 'Binary Search'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('recursion', 'Recursion'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashsets', 'Hashsets'), ('DFS', 'Depth First Search'), ('BFS', 'Breadth First Search'), ('backtracking', 'Backtracking')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('binary search', 'Binary Search'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('recursion', 'Recursion'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashsets', 'Hashsets'), ('DFS', 'Depth First Search'), ('BFS', 'Breadth First Search'), ('backtracking', 'Backtracking')], default='arrays'),
        ),
    ]
