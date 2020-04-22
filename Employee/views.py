from rest_framework import generics, viewsets, mixins
from .models import Member
from .serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class MemberGenViewset(viewsets.GenericViewSet, mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class MemberList(APIView):

    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        
        return Response( serializer.data)




