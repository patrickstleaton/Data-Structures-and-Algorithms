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
    ("trees", "Trees"),
    ("graphs", "Graphs"),
)


class Post(models.Model):
    author = models.TextField()
    title = RichTextField()
    category = models.TextField(choices = CATEGORY_CHOICES, default = 'arrays')
    difficulty = models.TextField(choices = DIFFICULTY_CHOICES, default = 'easy')
    description = RichTextField()
    text = RichTextField()
    explanation = RichTextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return str("{}'s article published on {}").format(self.author,
                                                          self.published_date)
