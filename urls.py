from django.urls import path
from .views import (
    observation_list,
    observation_detail,
    observation_create,
    observation_update,
    observation_delete
)

urlpatterns = [
    path('', observation_list, name='observation_list'),
    path('observation/<int:id>/', observation_detail, name='observation_detail'),
    path('observation/new/', observation_create, name='observation_create'),
    path('observation/<int:id>/edit/', observation_update, name='observation_update'),
    path('observation/<int:id>/delete/', observation_delete, name='observation_delete'),
]
