from django.contrib import admin
from .models import Person, Project, Experience, Education, Testimonial, SkillD, Skill


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PostAdmin)
admin.site.register(Project, PostAdmin)
admin.site.register(Experience, PostAdmin)
admin.site.register(Education, PostAdmin)
admin.site.register(Testimonial, PostAdmin)
admin.site.register(Skill, PostAdmin)
admin.site.register(SkillD, PostAdmin)


