from django.contrib import admin
from . models import PortforlioDetail,Projects,Comment,Stack,Framework,Cv,About
# Register your models here.

admin.site.register(PortforlioDetail)
admin.site.register(Projects)
admin.site.register(Comment)
admin.site.register(Stack)
admin.site.register(Framework)
admin.site.register(Cv)
admin.site.register(About)