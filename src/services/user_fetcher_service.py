import requests


class UserFetcherService:
    @staticmethod
    def get_users():
        r = requests.get('http://localhost:1080/users')
        return r.json()
