from django.urls import path
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='list'),
    path('add/', TeamMemberCreateView.as_view(), name='add'),
    path('edit/<slug:slug>/', TeamMemberUpdateView.as_view(), name='edit'),
    path('delete/<slug:slug>/', TeamMemberDeleteView.as_view(), name='delete'),
]
