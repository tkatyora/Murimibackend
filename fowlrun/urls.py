from django.urls import path
from . import views

urlpatterns = [
    path('view',views.ViewConditions_list),
    path('single/<int:pk>',views.SingleCondition),
]
