import configparser
config = configparser.RawConfigParser()
config.read('.\\configarations\\config.ini')


class ReadConfig():
    @staticmethod
    def getapplicationURL():
        urls = config.get('common info', 'urls')
        return urls


    @staticmethod
    def getUsername():
        username = config.get('common info',"username")
        return username


    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return  password
