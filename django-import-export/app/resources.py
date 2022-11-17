from import_export import resources
from app.models import Member

class MemberResource(resources.ModelResource):
    class Meta:
        model = Member