from django.dispatch import receiver 

from django.db.models.signals import pre_delete, pre_init, pre_save, post_save

import logging 


stdlogger = logging.getLogger(__name__)


@receiver(pre_save,sender='blog.Post')
def run_before_saving(sender, **kwargs):
    stdlogger.info('Start pre_save ')