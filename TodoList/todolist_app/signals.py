from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


@receiver(user_logged_in, sender=User)
def user_login_success(request, sender, user, **kwargs):
    print('Login success signal')


@receiver(user_logged_out, sender=User)
def user_logout_success(request, sender, user, **kwargs):
    print('User Logout Signal')


@receiver(user_login_failed)
def user_login_failed(request, sender, credentials, **kwargs):
    print('User Login failed Signal')


@receiver(pre_save, sender=User)
def pre_save_signal(sender, instance, **kwargs):
    print('User Model before save Signal')


@receiver(post_save, sender=User)
def post_save_signal(sender, instance, created, **kwargs):
    if kwargs.get('update_fields') == None and not created:
        user_cache = make_template_fragment_key('Navbar', [instance])
        cache.delete(user_cache)
    print('User Model after save Signal')
