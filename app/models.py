from django.db import models
from twilio.rest import Client


# Create your models here.


class Message(models.Model):
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=120)
    number = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        account_sid = 'AC165bb43e0d9cb8735ae3e1b328385d62'
        auth_token = '301a597040704a3b19a7fd6a42d0b89c'
        client = Client(account_sid, auth_token)
        if self.score <=70:
            message = client.messages.create(
                messaging_service_sid='MG46e600f236a6f5eb619cc99cf5829af6',

                body=f'{self.subject}\n\n'
                     f'{self.body}',
                to=f'{self.number}'
            )

            print(message.sid)
        return super().save(*args, **kwargs)
