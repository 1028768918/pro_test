import requests

if __name__ == '__main__':
    params = {'username': '10287689158', 'password': 'bmx199012'}
    x = requests.get("https://github.com/")
    print(x.text)

