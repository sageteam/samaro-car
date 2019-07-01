from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from dashboard.models import Rules
from dashboard.models import RulesCategory

class RulesCategorySerializer(ModelSerializer):
    class Meta:
        model = RulesCategory
        fields = ('sku', 'title', 'activate')
        read_only_fields = ('sku',)

class RulesSerializer(ModelSerializer):
    category = RulesCategorySerializer(required = True)
    class Meta:
        model = Rules
        fields = ('title', 'description', 'activate', 'category')
        read_only_fields = ('category',)

