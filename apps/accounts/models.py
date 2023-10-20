from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Teams(models.Model):
    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = "команды"

    rangeteam = range(100, 236)
    TEAM = [(i, i) for i in rangeteam]

    team = models.PositiveIntegerField(verbose_name='команда', choices=TEAM, default=1, null=True)

    def __str__(self):
        return str(self.team)

    def get_absolute_url(self):
        return reverse('oneteamstat', kwargs={'comanda': self.team})


class Profile(models.Model):
    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = "участники"



    GENDER = [
        ('м', "м"), ("ж", "ж")
    ]
    CATEGORY = [
        (1, 'Новичок - 50 км'), (2, 'Легкий - 100 км'), (3, 'Средний - 200 км'), (4, 'Тяжелый - 400 км'),
        (5, 'Ультра - 900 км')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Номер участника', db_index=True)
    runner_team = models.ForeignKey(Teams, on_delete=models.DO_NOTHING, verbose_name='команда')
    runner_age = models.IntegerField(verbose_name='возраст', null=False,default= 18, validators=[
        MaxValueValidator(80), MinValueValidator(18)
    ])
    runner_category = models.PositiveIntegerField(verbose_name='группа', choices=CATEGORY, default=1, db_index=True)
    runner_gender = models.CharField(max_length=1, choices=GENDER, verbose_name='пол участника', default='м')
    is_zabeg_2023 = models.BooleanField(verbose_name='Участник МыZaБег 2023', default=False)
    category_updated = models.PositiveIntegerField(verbose_name='Начальная группа', choices=CATEGORY,
                                                   default=0)
    completed = models.BooleanField(default=False, verbose_name="Выполнена квал-я")

    def __str__(self):
        return str(self.user)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    online = models.DateTimeField('Был в онлайне', null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_online_status(self):
        status = ''
        timezone_delta = timedelta(hours=3, minutes=0)
        online_status_true = timedelta(minutes=5)
        user_online = self.online + timezone_delta

        if self.user.profile.gender == 'F':
            if user_online.date() == (datetime.now() - timedelta(days=1)).date():
                status = 'Была онлайн вчера в ' + user_online.time().strftime("%H:%M")
            elif timezone.now() - self.online < online_status_true:
                status = 'Онлайн'
            elif user_online.date() == datetime.now().date():
                status = 'Была онлайн сегодня в ' + user_online.time().strftime("%H:%M")
            elif user_online.date().year == datetime.now().date().year:
                status = 'Была онлайн ' + user_online.date().strftime("%d.%m") + ' в ' + user_online.time().strftime(
                    "%H:%M")
            else:
                status = 'Была онлайн ' + user_online.date().strftime("%d.%m.%Y") + ' в ' + user_online.time().strftime(
                    "%H:%M")
        else:
            if user_online.date() == (datetime.now() - timedelta(days=1)).date():
                status = 'Был онлайн вчера в ' + user_online.time().strftime("%H:%M")
            elif timezone.now() - self.online < online_status_true:
                status = 'Онлайн'
            elif user_online.date() == datetime.now().date():
                status = 'Был онлайн сегодня в ' + user_online.time().strftime("%H:%M")
            elif user_online.date().year == datetime.now().date().year:
                status = 'Был онлайн ' + user_online.date().strftime("%d.%m") + ' в ' + user_online.time().strftime(
                    "%H:%M")
            else:
                status = 'Был онлайн ' + user_online.date().strftime("%d.%m.%Y") + ' в ' + user_online.time().strftime(
                    "%H:%M")
        return status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower_for = models.ForeignKey(User, related_name='follower_for', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

