from django.views.generic import TemplateView
from .models import Person, Project, Experience, Education, Testimonial, SkillD, Skill


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        context['projects'] = Project.objects.all()
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['skills'] = Skill.objects.all()
        context['skillds'] = SkillD.objects.all()
        return context
