import json
import requests
import copy
from sightingsPackage.sightingClass import Sighting

'''
Sightings
represents a group of recent bird sightings
'''

class Sightings():
    def __init__(self, regionCode):
        # calls the API using the API token and regionCode
        headers = {
          'X-eBirdApiToken': 'eatj08e790cn'
        }  
        url = f'https://api.ebird.org/v2/data/obs/{regionCode}/recent'
        response = requests.request('GET', url, headers=headers)
        
        # parses the API response into a list of dictionaries, creates a list of sightings sorted by time
        self.sightings = [Sighting(sighting) for sighting in json.loads(response.content)]
        self.sightings.sort(key=lambda sighting: sighting.obsDt)

    def __add__(self, sightings2):
        # copies current sightings object, adds sighting objects from sightings2, and sorts the result by time
        newSightings = copy.deepcopy(self)
        newSightings.sightings.extend(sightings2.sightings)
        newSightings.sightings.sort(key=lambda sighting: sighting.obsDt)
        return newSightings

    def __str__(self):
        output = ''
        for sighting in self.sightings:
            output += str(sighting) + '\n'
        return output
    
    def withinMiles(self, miles):
        # copies current sightings object with only sighting objects with distance <= miles
        newSightings = copy.deepcopy(self)
        newSightings.sightings = [sighting for sighting in newSightings.sightings if sighting.distance <= miles]
        return newSightings