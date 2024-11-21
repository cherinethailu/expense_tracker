from django.urls import path
from .views import (
    ExpenseListCreateView,
    ExpenseDetailView,
    ExpensesByDateRangeView,
    CategorySummaryView,
    UserCreateView
)

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expenses/by-date-range/', ExpensesByDateRangeView.as_view(), name='expenses-by-date-range'),
    path('expenses/category-summary/', CategorySummaryView.as_view(), name='category-summary'),
]
