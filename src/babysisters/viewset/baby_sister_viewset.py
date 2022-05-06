from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.utils.translation import gettext_lazy as _

from babysisters.models.baby_sister import BabySister
from babysisters.serializers.baby_sister_serializer import BabySisterSerializer, BabySisterListSerializer


class BabySisterViewSet(viewsets.ModelViewSet):
    queryset = BabySister.objects.all()
    serializer_class = BabySisterSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BabySisterListSerializer
        return BabySisterSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


EXAMPLE = (' ** { '
           '"name": string, '
           '"last_name": string, '
           '"document": "string", '
           '"phone": "string", '
           '"date_b": "dd/mm/yyyy" '
           ' } **')

BabySisterViewSet.__doc__ = """
list:
   {LIST}
create:
    {CREATE}
retrieve:
   {RETRIEVE} 
update:
    {UPDATE}
partial_update:
    {PARTIAL_UPDATE}
destroy:
    {DESTROY}
""".format(
    LIST=_("List of all baby sisters registered in the system."),
    CREATE=_("Create a baby sister data.") + EXAMPLE,
    RETRIEVE=_("Returns the information of a specific baby sister."),
    UPDATE=_("Update a baby sister data.") + EXAMPLE,
    PARTIAL_UPDATE=_("Partially update a baby sister data.") + ' ** { "name": "example name" } **',
    DESTROY=_("Destroy a baby sister data."),
)
