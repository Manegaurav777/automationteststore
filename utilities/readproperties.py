# import configparser
#
# config = configparser.RawConfigParser()
# config.read("Configuration/config.properties")
#
#
# class ReadConfig:
#     @staticmethod
#     def getadmin_pageurl():
#         url = config.get('admin info', 'https://automationteststore.com/index.php?rt=account/login')
#         return url
#
#     @staticmethod
#     def getusername():
#         username = config.get('admin info', 'Alex2019')
#         return username
#
#     @staticmethod
#     def getvalidPassword():
#         Validpassword = config.get('admin info', 'Alex2019@@')
#         return Validpassword
#
#     @staticmethod
#     def getInvlaidusername():
#         Invalidusername = config.get('admin info', 'admin@yourstore1.com')
#         return Invalidusername
