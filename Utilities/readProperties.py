#read data from ini file

import configparser
config = configparser.RawConfigParser()
config.read('.\\configuration\\config.ini')

class ReadConfig():
    @staticmethod
    def getUrl():
        url = config.get('common info', 'baseurl')
        return url
