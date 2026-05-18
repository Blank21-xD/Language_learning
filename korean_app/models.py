from django.db import models

# 1. User Table (For Broken Access Control demo)


class AppUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    # Storing plaintext/MD5 for insecure mode, but we will discuss hashing later
    password = models.CharField(max_length=255)
    # The target flag for access control
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# 2. Korean Dictionary Table (For SQL Injection demo)


class Dictionary(models.Model):
    korean_word = models.CharField(max_length=100)
    english_definition = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.korean_word} -> {self.english_definition}"

# 3. Community Forum Table (For XSS demo)


class ForumPost(models.Model):
    # Relates the post to our AppUser model
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    content = models.TextField()  # Where the malicious <script> tag will live
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"
