from base.views import BaseViewSet
from src.user import filters, serializers
from src.user.models import User


class UserViewSet(BaseViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.exclude(is_superuser=True).all()
    filterset_class = filters.UserFilter
    http_method_names = ["get", "post", "patch", "put"]


    def get_permissions(self):
        if self.action == 'create':
            # Disable authentication for create action
            return []
        return super().get_permissions()
