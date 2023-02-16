from django.db import models
import uuid

# Create your models here.


class BaseModel(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4())

    class Meta:
        abstract=True

class Accelerator(BaseModel):
    acc_title=models.CharField(max_length=200)
    acc_desc=models.CharField(max_length=500)
    acc_url=models.URLField()
    acc_img=models.ImageField()
    acc_doc=models.URLField()
    acc_video=models.URLField()
    acc_how_it=models.CharField(max_length=500)
    acc_no_of_days=models.IntegerField(default=0)
    acc_logo=models.ImageField()
