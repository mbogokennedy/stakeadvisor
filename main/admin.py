from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import BestTips, OurFavouritePick
from .resources import BestTipsResource


class BestTipsAdmin(ImportExportModelAdmin):
    list_display = ('kick_of_Time', 'home_Team', 'home_Percent', 'home_Odd', 'draw_Odd', 'away_Odd', 'away_Team', 'away_Percent', 'prediction')
    # resource_class = BestTipsResource

admin.site.register(BestTips, BestTipsAdmin)

class FavouritePickAdmin(admin.ModelAdmin):
    list_display = ('kick_of_Time', 'home_Team', 'away_Team', 'league', 'win_Percent', 'win_Odd', 'our_Pick', 'result')
    # resource_class = BestTipsResource

admin.site.register(OurFavouritePick, FavouritePickAdmin)
