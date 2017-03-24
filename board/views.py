from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, FormView
from board.forms import RegisterForm
from board.models import *

def GetSidebarStuff(user):
    content = {}
    content["username"] = user.username
    content["projects"] = Project.objects.filter(user_id=user).all()
    return content

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

class StoryCreate(CreateView):
    model = Story
    fields = ['project_id', 'status_id', 'user_id', 'sprint_id', 'description']
    template_name = 'create_story.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(StoryCreate, self).get_context_data(**kwargs)
        context['pk'] = int(self.kwargs['pk'])
        self.success_url = '/project/{}/' .format(int(self.kwargs['pk']))
        return context

class SprintCreate(CreateView):
    model = Sprint
    fields = ['project_id', 'duration', 'status']
    template_name = 'create_sprint.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(SprintCreate, self).get_context_data(**kwargs)
        context['pk'] = int(self.kwargs['pk'])
        self.success_url = '/project/{}/' .format(int(self.kwargs['pk']))
        return context

class ProjectView(DetailView):
    template_name = 'project.html'
    context_object_name = 'project'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['sidebar'] = GetSidebarStuff(self.request.user)
        sprints = list(enumerate(Sprint.objects.filter(project_id=self.object).all(), 1))
        stories = Story.objects.filter(project_id=self.object)
        context['sprints'] = [(i, sprint, stories.filter(sprint_id=sprint).all()) for i, sprint in sprints]
        return context
    