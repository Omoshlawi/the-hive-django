from django.utils.text import slugify
import os

STAKEHOLDER_MEDIA = 'stakeholders'


def agent_images(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (slugify(instance.name), ext)
    return os.path.join(STAKEHOLDER_MEDIA, slugify(instance.name), filename)

