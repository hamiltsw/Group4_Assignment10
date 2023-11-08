from datetime import datetime, timedelta
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
            self.obsDt = datetime.strptime(sighting['obsDt'], '%Y-%m-%d %H:%M')
        except ValueError:
            self.obsDt = datetime.strptime(sighting['obsDt'][:10], '%Y-%m-%d')        # if time is not included, only the date is set
        
    def __str__(self):
        # adjusts the text for whether there were multiple birds sighted or not
        plural = {True: 's were', False: ' was'}[self.howMany > 1]
        
        # adjusts the text for whether the sighting was minutes, hours, or days ago
        difference = datetime.now() - self.obsDt
        if difference.days >= 1:
            time = f'{difference.days} days'
        elif difference.seconds // 3600 >= 2:
            time = f'{difference.seconds // 3600} hours'
        else:
            time = f'{difference.seconds // 60} minutes'
        
        return f"{self.howMany} {self.comName}{plural} spotted {self.distance} miles away {time} ago!"    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    