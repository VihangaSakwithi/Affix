from rest_framework import serializers
from proworkerApp.models import ProWorkers

class ProworkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProWorkers
        fields=('ProWorkerId', 'ProWorkerName', 'UrbanCity', 'JoinDate', 'ImageName')