from rest_framework import serializers

from .models import Country

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('state', 'district','city')




