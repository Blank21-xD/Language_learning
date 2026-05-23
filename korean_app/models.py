from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Vocabulary(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hangul = models.CharField(max_length=100)
    romanization = models.CharField(max_length=100)
    definition = models.TextField()

    def __str__(self):
        return self.hangul


class UserProfilereview(models.Model):
    username = models.CharField(max_length=100)
    learning_goal = models.TextField()
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class GuestBookComment(models.Model):
    author = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
