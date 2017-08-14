from django.contrib import admin
from .models import UserJournal
# Register your models here.


class adminUserJournal(admin.ModelAdmin):
    list_display = ('usr_name', 'work_today', 'question', 'plan_tomorrow', 'date')

    # fieldsets = [
    #     (None, {'fields': ['usr_name', ]}),
    #     ('日志内容', {'fields': ['work_today', 'question', 'plan_tomorrow']})
    # ]


admin.site.register(UserJournal, adminUserJournal)

admin.AdminSite.site_header = "日志管理小站"
admin.AdminSite.site_title = "小站"
