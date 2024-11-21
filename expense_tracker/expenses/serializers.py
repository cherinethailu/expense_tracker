from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ExpenseSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'user_id', 'user', 'title', 'amount', 'date', 'category']

    def validate_amount(self, value):
        """
        Ensure the expense amount is a positive number.
        """
        if value <= 0:
            raise serializers.ValidationError("Expense amount must be a positive number.")
        return value

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"user_id": "User with this ID does not exist."})

        expense = Expense.objects.create(user=user, **validated_data)
        return expense
