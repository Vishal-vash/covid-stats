from django.db import models


# Create your models here.
class Stats(models.Model):
    country = models.CharField(max_length=200)
    country_iso = models.CharField(max_length=3)
    lat = models.FloatField(null=True)
    lang = models.FloatField(null=True)
    flag = models.CharField(max_length=200)
    cases = models.IntegerField(null=True)
    todayCases = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    todayDeaths = models.IntegerField(null=True)
    recovered = models.IntegerField(null=True)
    todayRecovered = models.IntegerField(null=True)
    active = models.IntegerField(null=True)
    critical = models.IntegerField(null=True)
    casesPerOneMillion = models.IntegerField(null=True)
    deathsPerOneMillion = models.IntegerField(null=True)
    tests = models.IntegerField(null=True)
    testsPerOneMillion = models.IntegerField(null=True)
    population = models.IntegerField(null=True)
    continent = models.CharField(max_length=200)
    oneCasePerPeople = models.IntegerField(null=True)
    oneDeathPerPeople = models.IntegerField(null=True)
    oneTestPerPeople = models.IntegerField(null=True)
    activePerOneMillion = models.FloatField(null=True)
    recoveredPerOneMillion = models.FloatField(null=True)
    criticalPerOneMillion = models.FloatField(null=True)

    def __str__(self):
        return self.country
