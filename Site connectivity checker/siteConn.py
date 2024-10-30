import urllib.request as ulib

def siteConnection(url):
    response = ulib.urlopen(url)
    print('Connected to ' + url + 'successfully.')
    print('The respose code was:', response.getcode())

input_url = input('Enter an URL: ')
siteConnection(input_url)    