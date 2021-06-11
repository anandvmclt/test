from django.db import models
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    profile_img = models.FileField(upload_to="profile_img/", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.profile_img:
            filename = "%s.jpg" % self.profile_img.name.split('.')[0]
            img = Image.open(BytesIO(self.profile_img.read()))


            if img.mode == "RGBA":
                img = img.convert("RGB")
            output = BytesIO()
            img.save(output, format='PDF', quality=100)
            output.seek(0)
            self.profile_img = InMemoryUploadedFile(output, 'ImageField', "%s.pdf" % self.profile_img.name.split('.')[0],
                                              'application/pdf', output.len, None)
            # output = "output.pdf"
            # image = img.save(output, "PDF", resolution=100.0)
            # image_io = BytesIO(image)
            # self.profile_img.save(output, ContentFile(image_io.getvalue()), save=False)
        super(Employees, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
