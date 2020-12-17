# Generated by Django 3.0.2 on 2020-12-11 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201126_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alt_category',
            field=models.TextField(blank=True, choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('binary search', 'Binary Search'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('recursion', 'Recursion'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashsets', 'Hashsets'), ('DFS', 'Depth First Search'), ('BFS', 'Breadth First Search'), ('backtracking', 'Backtracking'), ('greedy', 'Greedy')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('binary search', 'Binary Search'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('recursion', 'Recursion'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashsets', 'Hashsets'), ('DFS', 'Depth First Search'), ('BFS', 'Breadth First Search'), ('backtracking', 'Backtracking'), ('greedy', 'Greedy')], default='arrays'),
        ),
    ]