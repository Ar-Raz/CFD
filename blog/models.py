from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.jpg', '.png', ]
    if not ext.lower() in valid_extension:
        raise ValidationError('Unsupported file format')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar', null= True, blank=True, validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=32)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False)
    cover = models.FileField(upload_to='files/catergory_cover', null=False, blank=False, validators=[validate_file_extension])
