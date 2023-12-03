from django.urls import path
from team_manager.views import TeamMemberListView, TeamMemberCreateView

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='list'),
    path('add/', TeamMemberCreateView.as_view(), name='add'),
]