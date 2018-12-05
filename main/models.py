from django.db import models

# Create your models here.

class BestTips(models.Model):
    kick_of_Time = models.CharField(max_length=100)
    home_Team = models.CharField(max_length=100)
    home_Percent = models.CharField(max_length=100)
    home_Odd = models.CharField(max_length=100)
    draw_Odd = models.CharField(max_length=100)
    away_Odd = models.CharField(max_length=100)
    away_Team = models.CharField(max_length=100)
    away_Percent = models.CharField(max_length=100)
    prediction = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Best Tips"
        ordering = ["-home_Odd",]

    def __str__(self):

        return(self.home_Team)

class OurFavouritePick(models.Model):
    kick_of_Time = models.CharField(max_length=100)
    home_Team = models.CharField(max_length=100)
    away_Team = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    win_Percent = models.CharField(max_length=100)
    win_Odd = models.CharField(max_length=100)
    our_Pick = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Our Favourite Picks"

    def __str__(self):

        return(self.home_Team)
