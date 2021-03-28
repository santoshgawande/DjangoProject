from django.db import models

# Create your models here.
class Equity(models.Model):

    code = models.IntegerField()
    name = models.CharField(max_length=255)

    open = models.FloatField(max_length=255)
    high = models.CharField(max_length=255)

    low = models.FloatField(max_length=255)
    close = models.CharField(max_length=255)

    class Meta(object):
        app_label = 'stock'
        default_related_name = 'equities'

    def __unicode__(self):
        return self.name
 
    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close
        }
