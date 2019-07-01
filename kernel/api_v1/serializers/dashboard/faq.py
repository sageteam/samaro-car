from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from dashboard.models import FAQ
from dashboard.models import FAQCategory

class FAQCategorySerializer(ModelSerializer):
    class Meta:
        model = FAQCategory
        fields = ('sku', 'title', 'activate')
        read_only_fields = ('sku',)

class FAQSerializer(ModelSerializer):
    category = FAQCategorySerializer(required = True)

    class Meta:
        model = FAQ
        fields = ('title', 'description', 'activate', 'category')
        read_only_fields = ('category',)
