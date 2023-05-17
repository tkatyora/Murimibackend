from rest_framework import serializers
from .models import FowlRunConditions

class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FowlRunConditions()
        fields = '__all__'
        #fields = ['id','temperature','humidity','date_recorded','date_update']