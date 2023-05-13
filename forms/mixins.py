from django.shortcuts import get_object_or_404


class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        multi_filter = {field: self.kwargs[field] for field in self.lookup_fields}
        obj = get_object_or_404(queryset, **multi_filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
