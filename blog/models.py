from django.db import models
from django.utils import timezone

# Author
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Category
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

# Post
class Post(models.Model):
    PUBLISHED = 1
    DRAFT = 0
    UNLISTED = -1

    status_choices = [
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (UNLISTED, 'Unlisted'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="posts", blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    date_available = models.DateTimeField(default=timezone.now)
    sort_order = models.IntegerField(default=0)
    status = models.SmallIntegerField(default=DRAFT, choices=status_choices)
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    date_modified = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        self.date_modified = timezone.now()

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.description[:50]
