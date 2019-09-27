from django.contrib import admin


from .models import Center

from .models import Ranks,question,Send,Aptitude,SendEmail,CCAT_Question

admin.site.register(question)
admin.site.register(Center)
admin.site.register(Ranks)
admin.site.register(Send)
admin.site.register(CCAT_Question)
admin.site.register(Aptitude)
admin.site.register(SendEmail)


