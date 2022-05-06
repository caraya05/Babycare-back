from loducode_utils.serializers import AuditSerializer

from babysisters.models.baby_sister import BabySister


class BabySisterSerializer(AuditSerializer):
    class Meta:
        model = BabySister
        fields = ('id', 'name', 'last_name', 'document', 'phone', 'date_b',)


class BabySisterListSerializer(AuditSerializer):
    class Meta:
        model = BabySister
        fields = ('id', 'name', 'last_name', 'phone')


class BabySisterCreateSerializer(AuditSerializer):
    class Meta:
        model = BabySister
        fields = ('name', 'last_name', 'document', 'phone', 'date_b',)
