from django.contrib import admin

from apps.models import Comment


class EventAdminSite(admin.AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"


event_admin_site = EventAdminSite(name='event_admin')

event_admin_site.register(Comment)
