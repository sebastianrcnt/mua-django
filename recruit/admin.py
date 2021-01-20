from django.contrib import admin
from .models import Application, Part, Question, Evaluation, EvaluationCriteria, Recruit, Answer

# Register your models here.
admin.site.register(Application)
admin.site.register(Part)
admin.site.register(Question)
admin.site.register(Evaluation)
admin.site.register(EvaluationCriteria)
admin.site.register(Recruit)
admin.site.register(Answer)
