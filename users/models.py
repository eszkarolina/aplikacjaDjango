from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
import string
import requests
from django.conf import settings


# Returns a random alphanumeric string of length 'length'
def generate_profile_secret(length):
    key = ''
    for i in range(length):
        key += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    return key


def send_email(email_address, body, subject=u"Activation email"):
    return requests.post(
        "https://api.mailgun.net/v2/%s/messages" % settings.MAILGUN_DOMAIN,
        auth=("api", settings.MAILGUN_API_KEY),
        data={"from": "JTEST <abc@samples.mailgun.org>",
              "to": [email_address],
              "subject": subject,
              "text": body})

def send_activation_email(user):
    
    secret=user.profile.secret
    email=user.email
    string="http://127.0.0.1:8000/users/activate/"+secret
    send_email(email, string)
	





class Profile(models.Model):

    class Meta:
        verbose_name = 'User profile'

    user = models.OneToOneField(User)
    secret = models.CharField(max_length=50)

    def __unicode__(self):
        return 'Profile for %s' % self.user.username


    @receiver(post_save, sender=User)
    def create_user_profile(sender, **kwargs):
        if kwargs.get('created', False):
            profile = Profile.objects.create(
                          user = kwargs.get('instance'),
                          secret = generate_profile_secret(50)
                      )
            send_activation_email(kwargs.get('instance'))


    

