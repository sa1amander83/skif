from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.accounts.models import Profile, Teams


class UserImport(models.Model):
    csv_file = models.FileField(upload_to='uploads/')


def user_directory_path(instance, filename):
    runner = instance.runner.user.username
    subdiv = runner[:3]
    return 'day_of_month/{0}/{1}/{2}/{3}'.format(instance.day_select, subdiv, runner, filename)





class Image(models.Model):
    image = models.FileField(verbose_name="фото", upload_to=user_directory_path, null=False,
                             blank=False, max_length=300, unique=True)


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')


class SkierDay(models.Model):
    class Meta:
        verbose_name = 'ежедневный забег'
        verbose_name_plural = "пробеги по дням"

    class SkierDayObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    day_today = datetime.now().day
    # days = range(datetime.now().day, 31)
    days = range(1, 31)

    DAYS = [(i, i) for i in days]

    date_insert = models.DateTimeField(verbose_name="дата внесения пробежки", auto_now_add=True)
    runner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='участник', related_name='runner',
                               db_index=True)
    day_select = models.IntegerField(verbose_name='день пробега', choices=DAYS, default=day_today, db_index=True)
    day_distance = models.FloatField(verbose_name='дистанция за пробежку', help_text='введите в формате 10,23',
                                     db_index=True)
    day_time = models.TimeField(verbose_name='введите время пробежки', help_text='введите в формате 00:00:00',
                                db_index=True)
    day_average_temp = models.TimeField(verbose_name='средний темп', help_text='введите в формате 00:00:00',
                                        db_index=True)
    photo = models.ForeignKey(Image, on_delete=models.CASCADE)
    # photo = models.ForeignKey(Image, on_delete=models.CASCADE)
    #                           #                           blank=False, max_length=300,  unique=True)
    calory = models.IntegerField(verbose_name='Потрачено калорий', null=True if day_today != 16 else False,
                                 blank=True if day_today != 16 else False, db_index=True)

    skirun_like = models.ManyToManyField(User,
                                       related_name='skirun_liked',
                                       blank=True)
    skirun_dislike = models.ManyToManyField(User,
                                          related_name='skirun_disliked',
                                          blank=True)
    objects=models.Manager()
    skiobjects=SkierDayObjects()



    def __str__(self):
        return str(self.runner)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})


class KeyWordClass(models.Model):
    kwteam = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name='команда')
    keyword = models.CharField(verbose_name='кодовое слово', max_length=20)

    def __str__(self):
        return str(self.keyword)

    class Meta:
        verbose_name = "Ключевые слова"
        verbose_name_plural = "Ключевые слова"


class Like(models.Model):
    LIKE_OR_DISLIKE_CHOICES = (
        ("LIKE", "like"),
        ("DISLIKE", "dislike"),
        (None, "None")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    for_skier = models.ForeignKey(Profile, on_delete=models.CASCADE)
    like_or_dislike = models.CharField(max_length=7,
                                       choices=LIKE_OR_DISLIKE_CHOICES,
                                       default=None)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Comment(models.Model):
    post = models.ForeignKey(SkierDay, on_delete=models.CASCADE, related_name="post_comments")
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField('Текст комментария', max_length=350)
    comment_pubdate = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
