from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class NoOutgoingConnections(models.Model):
    pass


class ProxyNode2(NoOutgoingConnections):
    class Meta:
        proxy = True


class ProxyNode(NoOutgoingConnections):
    class Meta:
        proxy = True


class GenericFK(models.Model):
    content_type = models.ForeignKey(
        "contenttypes.ContentType", on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
