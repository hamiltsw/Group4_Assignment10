# Names: Stewart Hamilton, James Speed
# emails: hamiltsw@mail.uc.edu, speedjp@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/09/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: Working with API calls
# Citations: 
#     Distance function adapted from https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
#     API documentation: https://documenter.getpostman.com/view/664302/S1ENwy59
# Anything else that's relevant:

from sightingsPackage.sightingsClass import Sightings

if __name__ == '__main__':
    # prints recent bird sightings from Ohio and Kentucky within 50 miles
    print((Sightings('US-OH') + Sightings('US-KY')).withinMiles(50))
