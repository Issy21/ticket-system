from django.contrib import admin
from .models import Ticket
# Adapted from:
# W3Schools (n.d.) Django Admin.
# Available at: https://www.w3schools.com/django/django_admin.php
# (Accessed: 4 June 2026).
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')  # details of admiin managed tickets
