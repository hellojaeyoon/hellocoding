from django.contrib import admin

from .models import Review # 명시적 상대경로 표현

# Register your models here.
admin.site.register(Review)
