from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from site_back.users.models import User
from site_back.users.services import user_create


@admin.register(User)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_superuser', 'is_active', 'created_at', 'updated_at')

    search_fields = ('email', 'username',)

    list_filter = ('is_active', 'is_admin', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'username')}),
    )

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)

        try:
            user_create(**form.cleaned_data)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
