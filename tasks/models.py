from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=70)
    description = models.TextField()
    term = models.DateField()
    is_completed = models.BooleanField(default=False)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='tasks/covers/%Y/%m/%d/', blank=True, default='tasks/task-img.jpg')
    days_to_alert = models.IntegerField(default=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name
