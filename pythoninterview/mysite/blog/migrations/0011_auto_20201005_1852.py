# Generated by Django 3.0.2 on 2020-10-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201005_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alt_category',
            field=models.TextField(blank=True, choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashset', 'Hashset')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(choices=[('arrays', 'Arrays'), ('strings', 'Strings'), ('linked lists', 'Linked Lists'), ('trees', 'Trees'), ('DP', 'Dynamic Programming'), ('math', 'Math'), ('graphs', 'Graphs'), ('stacks', 'Stacks'), ('queues', 'Queues'), ('tries', 'Tries'), ('heaps', 'Heaps'), ('hashmaps', 'Hashmap'), ('binary', 'Binary'), ('hashset', 'Hashset')], default='arrays'),
        ),
    ]
