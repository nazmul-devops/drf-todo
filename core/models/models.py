from model_utils import FieldTracker
from model_utils.models import TimeStampedModel
from django.db import IntegrityError


class BaseTimeStampedModel(TimeStampedModel):
    tracker = FieldTracker()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        try:
            super().delete(**kwargs)
        except IntegrityError:
            raise "Integrity Error"