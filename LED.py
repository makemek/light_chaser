class Rgb_Led:
    
    def __init__(self, rgbVal=0):
        ''' retrieve integer value containing 3 rgb channels
        1st byte = blue
        2nd byte = green
        3rd byte = red'''
        self.__rgbVal = rgbVal

    def storeState(self, rgbVal):
        self.__rgbVal = rgbVal

    def retrieveLastState(self):
        return self.__rgbVal