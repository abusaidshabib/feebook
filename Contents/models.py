from django.db import models
from authentication.models import BaseModel, CustomUser

class Photo(BaseModel):
    url = models.ImageField(upload_to='post_pictures/',blank=True, height_field=None, width_field=None, max_length=None)
 
class Post(BaseModel):
    
    user = models.ForeignKey(CustomUser, related_name="user", on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ForeignKey(Photo, blank=True)
    video = models.FileField(upload_to='post_video/', max_length=100)
    likes = models.CharField(max_length=10,choices=[('likes','Likes'),('love','Love'),('sad', 'Sad'),('wow', 'Wow')])


class Comment(BaseModel):
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name="user", on_delete=models.CASCADE)
    comment = models.TextField()
    reply = models.TextField()
    replied_user = models.ForeignKey(CustomUser, related_name="replied_user", on_delete=models.CASCADE)


