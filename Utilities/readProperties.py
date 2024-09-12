import configparser

config = configparser.RawConfigParser()
file_path="C:\\Users\\Dudes co\\Desktop\\E-commerce\\Configurations\\config.ini"
config.read(file_path)
# config.read(".\\Configurations\\config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        print(config.sections())
        url = config.get('common','baseURL')
        print(url)
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common', 'password')
        return password