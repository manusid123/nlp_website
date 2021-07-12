from django.contrib import admin
from home.models import Contact,Summarize,Generation,Sentiment,Question
# Register your models here.

admin.site.register(Contact)
admin.site.register(Summarize)
admin.site.register(Generation)
admin.site.register(Sentiment)
admin.site.register(Question)