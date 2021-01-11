from io import BytesIO
import logging 
from PIL import Image 
from django.core.files.base import ContentFile 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ProductImage

THUMBNAIL_SIZE = (300, 300)

logger = logging.getLogger(__name__)

@receiver(pre_save, sender=ProductImage)
def generate_thumbnail(sender, instance, **kwargs):
    logger.info(
        f'Generating thumbnail for product {instance.product.id}'
    )
    image = Image.open(instance.image)
    image = image.convert('RGB')
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

    temp_thumb = BytesIO()
    image.save(temp_thumb, 'JPEG')
    temp_thumb.seek(0)
    # set save=False, otherwise it will run in an infinite loop
    instance.thumbnail.save(
        instance.image.name, 
        ContentFile(temp_thumb.read()),
        save=False,
    )
    temp_thumb.close()

'''
Once we have done this, we need to make sure this file is initialized
when the Django application is launched by the internal Django
application registry. The suggested way to do this is to add a method called
ready() in the application config inside main/apps.py:
'''

