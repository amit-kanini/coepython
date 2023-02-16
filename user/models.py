from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4())

    class Meta:
        abstract=True


class User(BaseModel):
    first_name:models.CharField(max_length=200)
    email:models.URLField()
    password:models.CharField()
    is_admin:models.BooleanField(default=False)
    status:models.CharField(default="Pending")
    login_counter:models.IntegerField(default=0)
