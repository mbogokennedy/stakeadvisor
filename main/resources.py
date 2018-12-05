from .models import BestTips
from import_export import resources
class BestTipsResource(resources.ModelResource):
    class Meta:
        model = BestTips