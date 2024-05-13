from rest_framework.permissions import IsAuthenticated


class ProductQuerySetMixin:

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        queryset = queryset.filter(store=user)
        return queryset


class AuthenticationMixin:
    permission_classes = [IsAuthenticated]