from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

DIFFICULTY_CHOICES = (
    ("easy", "Easy"),
    ("medium", "Medium"),
    ("hard", "Hard"),
)

CATEGORY_CHOICES = (
    ("arrays", "Arrays"),
    ("strings", "Strings"),
    ("linked lists", "Linked Lists"),
    ("binary search", "Binary Search"),
    ("trees", "Trees"),
    ("DP", "Dynamic Programming"),
    ("math", "Math"),
    ("recursion", "Recursion"),
    ("graphs", "Graphs"),
    ("stacks", "Stacks"),
    ("queues", "Queues"),
    ("tries", "Tries"),
    ("heaps", "Heaps"),
    ('hashmaps', 'Hashmap'),
    ('binary', 'Binary'),
    ('hashsets', 'Hashsets'),
)

class Post(models.Model):
    author = models.TextField()
    title = RichTextField()
    category = models.TextField(choices = CATEGORY_CHOICES, default = 'arrays')
    alt_category = models.TextField(choices = CATEGORY_CHOICES, blank=True, null = True)
    difficulty = models.TextField(choices = DIFFICULTY_CHOICES, default = 'easy')
    description = RichTextField()
    text = RichTextField()
    explanation = RichTextField()
    additional_notes = RichTextField(blank=True, null = True)
    published_date = models.DateTimeField(blank=True, null=True)


    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.title.strip("<p>").strip("</p>"))
