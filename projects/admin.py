from django.contrib import admin
from .models import Customer, Project, Payment, WorkTeam, Schedule, NewsPost


admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Payment)
admin.site.register(WorkTeam)
admin.site.register(Schedule)
admin.site.register(NewsPost)
