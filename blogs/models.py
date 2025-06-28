from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices = [
        ("tech", "Technology"),
        ("life", "Lifestyle"),
        ("edu", "Education"),
        ("travel", "Travel"),
        ("food", "Food"),
        ("news", "News"),
        ("finance", "Finance"),
        ("health", "Health & Wellness"),
        ("sports", "Sports"),
        ("code", "Programming"),
        ("art", "Art & Design"),
        ("business", "Business"),
        ("gaming", "Gaming"),
        ("science", "Science"),
        ("books", "Books & Literature"),
        ("music", "Music"),
        ("movies", "Movies & TV"),
        ("personal", "Personal Development"),
    ],default=('tech','technology'))
    description = models.CharField(max_length=300)
    date = models.DateTimeField()
    author = models.CharField(max_length=100)
    content = HTMLField()
    image = models.FileField(
        upload_to="news_img/", max_length=240, null=True, default=None
    )
