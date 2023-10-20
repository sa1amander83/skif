from os import path

from django.contrib import admin

# Register your models here.
class TeamsAdmin(admin.ModelAdmin):
    # team=fields.Field(column_name='team', attribute='team',widget=ForeignKeyWidget(Teams,'team'))
    search_fields = ('team',)
    list_display = ('team',)
    list_display_links = ('team',)

    list_filter = ('team',)
    ordering = ('team',)
    list_per_page = 100
    list_max_show_all = 100
    # class Meta:


# class RunnerAdmin(ImportExportActionModelAdmin):
class RunnerAdmin(admin.ModelAdmin):
    # resource_class = TeamsAdmin
    # def пробег_за_день(self, username, day_distance=None):
    #     result = RunnerDay.objects.filter(user__user__username=username).filter(
    #         user__runnerday__day_distance=day_distance)
    #
    #     return result
    #
    # def дистанция_за_день(self, username):
    #     result = RunnerDay.objects.filter(user__user__username=username)
    #     return result
    #
    # def время_пробега(self, username):
    #     result = RunnerDay.objects.filter(user__user__username=username)
    #     return result
    #
    # def средний_темп(self, username):
    #     result = RunnerDay.objects.filter(user__user__username=username)
    #     return result

    # fields = ('пробег_за_день', 'дистанция_за_день', 'время_пробега', 'средний_темп',)
    search_fields = (
    'user__username', 'runner_team__team', 'runner_age', 'runner_category', 'runner_gender', 'completed','is_admin')
    list_editable = ('runner_age', 'runner_category', 'runner_gender', 'is_admin','completed','category_updated')
    list_display = ('user', 'runner_team', 'runner_age', 'runner_category', 'runner_gender', 'completed','is_admin','category_updated')
    # 'пробег_за_день','дистанция_за_день', 'время_пробега', 'средний_темп',)
    # list_display = ('user', 'runner_age', 'runner_category', 'runner_gender', 'is_admin', 'пробег_за_день', )
    list_display_links = ('user', 'runner_team')

    list_filter = ('runner_category', 'completed','runner_team','category_updated')
    ordering = ('user',)

    list_per_page = 100
    list_max_show_all = 100

    # def get_urls(self):
    #     urls = super().get_urls()
    #     urls.insert(-1, path('csv-upload/', self.upload_csv))
    #     urls.insert(-1, path('update_data/', update_data))
    #     return urls


class RunnerDayAdmin(admin.ModelAdmin):
    days = range(1, 31)
    DAYS = [(i, i) for i in days]
    search_fields = ('runner__user__username','day_select', 'day_distance', 'day_time', 'day_average_temp',
                     )
    list_editable = ('day_distance', 'day_select','day_time', 'day_average_temp',
                     )
    list_display = ('runner','day_select', 'day_distance', 'day_time', 'day_average_temp','date_insert'
                    )
    list_display_links = ('runner',)

    list_per_page = 100
    list_max_show_all = 100