from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kids/', views.KidListView.as_view(), name='kids'),
    path('kids/<int:pk>', views.KidDetailView.as_view(), name='kid-detail'),
    path('kid/create/', views.KidCreate.as_view(), name='kid-create'),
    path('kids/<int:pk>/update/', views.KidUpdate.as_view(), name='kid-update'),
    path('kids/<int:pk>/delete/', views.KidDelete.as_view(), name='kid-delete'),
    path('rules/', views.RuleListView.as_view(), name='rules'),
    path('rules/<int:pk>', views.RuleDetailView.as_view(), name='rule-detail'),
    path('rule/create/', views.RuleCreate.as_view(), name='rule-create'),
    path('rules/<int:pk>/update', views.RuleUpdate.as_view(), name='rule-update'),
    path('rules/<int:pk>/delete', views.RuleDelete.as_view(), name='rule-delete'),
    path('rule-instance/create/', views.RuleInstanceCreate.as_view(), name='rule-instance-create')
]