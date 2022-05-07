from datetime import datetime
from django.db import models
import datetime


# -------------------------------------------------------------------
# database file upload model :
class FileUploadModel(models.Model):
    id = models.AutoField(primary_key=True)
    fileName = models.FileField(upload_to='files')
    dateUpload = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.dateUpload
