"""
Serialization definitions.

I.e., how our python models should be converted to text format (what fields are specified, etc.)
"""
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import serializers

from beanserver.beanapi.models import Expense


class UserSerializer(serializers.HyperlinkedModelSerializer[User]):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class GroupSerializer(serializers.HyperlinkedModelSerializer[Group]):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ExpenseSerializer(serializers.Serializer[Expense]):
    cost = serializers.FloatField()

    def create(self, validated_data):
        return Expense.objects.create(**validated_data)
