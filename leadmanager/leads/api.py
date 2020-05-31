from leads.models import Leads
from rest_framework import viewsets,permissions
from .serializers import LeadSerializers

#lead viewsets
class LeadViewSet(viewsets.ModelViewSet):
    # queryset = Leads.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class  = LeadSerializers

    def get_queryset(self):
        return  self.request.user.all.leads.all()
    
    
    def perform_create(self,serializers):
        serializers.save(owner=self.request.user)
        