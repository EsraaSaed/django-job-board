from rest_framework import   serializers#routers, #viewsets
from.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


