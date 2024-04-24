from rest_framework.filters import BaseFilterBackend

class FriendListFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        request_type = request.query_params.get(
            "request_type", ""
        )
        if request_type.lower() == 'accepted':
            return queryset.filter(status=2)
        return queryset.filter(status=1)
