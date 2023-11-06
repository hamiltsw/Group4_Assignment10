import datetime
from utilsPackage.utils import distance

'''
Sighting
represents a recent bird sighting
'''

class Sighting():
    def __init__(self, sighting):
        lindLat, lindLng = 39.13373265321474, -84.51453910014975                               # coordinates of Lindner College of Business
        
        # gets relevant variables from sighting dictionary
        self.comName = sighting['comName']                                                     # name of the bird sighted
        self.distance = round(distance(lindLat, lindLng, sighting['lat'], sighting['lng']), 1) # distance from sighting to Lindner College of Business
        self.howMany = sighting.get('howMany', 1)                                              # how many birds were sighted
        try:                                                                                   # date and time of the sighting
            self.obsDt = datetime.datetime.strptime(sighting['obsDt'], '%Y-%m-%d %H:%M')
        except ValueError:
            self.obsDt = datetime.datetime.strptime(sighting['obsDt'][:10], '%Y-%m-%d')        # if time is not included, only the date is set
        
    def __str__(self):
        plural = {True: 's were', False: ' was'}[self.howMany > 1] # adjusts the text for whether multiple birds were sighted or not
        date = self.obsDt.strftime('%m/%d/%Y')
        time = self.obsDt.strftime('%H:%M')
        return f"{self.howMany} {self.comName}{plural} spotted {self.distance} miles away on {date} at {time}!"