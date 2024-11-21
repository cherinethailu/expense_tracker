from rest_framework import generics, views, status
from rest_framework.response import Response
from .models import Expense, User
from .serializers import ExpenseSerializer, UserSerializer
from django.db.models import Sum
from datetime import datetime

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpensesByDateRangeView(views.APIView):
    def get(self, request):
        user_id = request.query_params.get('user')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if not (user_id and start_date and end_date): # making sure we have all the fields
            return Response({"error": "Missing required parameters."}, status=status.HTTP_400_BAD_REQUEST)

        expenses = Expense.objects.filter(
            user_id=user_id, date__range=[start_date, end_date]
        )
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

class CategorySummaryView(views.APIView):
    def get(self, request):
        user_id = request.query_params.get('user')
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        if not (user_id and month and year): # do we have all the fields ??
            return Response({"error": "Missing required parameters."}, status=status.HTTP_400_BAD_REQUEST)

        expenses = Expense.objects.filter(
            user_id=user_id, date__year=year, date__month=month
        ).values('category').annotate(total=Sum('amount'))

        return Response(expenses)
