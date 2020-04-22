from rest_framework import serializers
from .models import Member, ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = (
                    'start_time',
                    'end_time'
                 )



class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)
    class Meta:
        model = Member
        fields = [ 
            'id',
            'real_name',
            'tz',
            'activity_periods',    
        ]
        depth = 1
