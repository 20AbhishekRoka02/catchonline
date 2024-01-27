from django.db import models
import uuid
# Create your models here.
class Query(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    message=models.TextField("message")
    # voice = models.FileField("voice_clip", upload_to=None, max_length=100)

    def save(self, *args, **kwargs):
        # Call the parent class's save method to perform the actual save operation
        super().save(*args, **kwargs)

        # Access the user ID after saving
        query_id = self.id
        return str(query_id)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "query"
        verbose_name_plural = "queries"

class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    message=models.TextField("message")

    def save(self, *args, **kwargs):
        # Call the parent class's save method to perform the actual save operation
        super().save(*args, **kwargs)

        # Access the user ID after saving
        test_id = self.id
        return str(test_id)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"