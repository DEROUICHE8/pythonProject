
from django.core.mail import send_mail
from django.db import models

# Create your models here.
from django.db import models
class Dht11(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp > 20:
            from DHT.views import sendtele

            sendtele(self.temp, self. hum)
            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine le,' + str(self.dt),
                'derouich.adnane123@gmail.com',
                ['ahmedmotiebachir2000@gmail.com'],
                fail_silently=False,
            )

        return super().save(*args, **kwargs)

