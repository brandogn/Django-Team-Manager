from django.shortcuts import render,  redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TeamMember
from .forms import TeamMemberForm


# Create your views here.
class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'list.html'
    context_object_name = 'team_members'


class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_message'] = "Add a team member"
        context['sub_message'] = "Set email, location and role."
        context['view_type'] = "Add"
        return context


class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_message'] = "Edit team member"
        context['sub_message'] = "Edit contact info, location and role."
        context['view_type'] = "Edit"
        return context


class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    template_name = 'form.html'

    # Redirect to the list page after successful deletion
    success_url = reverse_lazy('list')
