from django.shortcuts import render
from django.views.generic import ListView, CreateView
from team_manager.models import TeamMember
from team_manager.forms import TeamMemberForm


# Create your views here.


class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'list.html'
    context_object_name = 'team_members'

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'add.html'
    success_url = '/'
