from rest_framework import serializers
from .models import Test

class TestSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Test
        fields = ('id', 'question', 'variant_a', 'variant_b', 'variant_c', 'correct_answer')