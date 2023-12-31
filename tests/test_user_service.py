from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService
from Utilities.utility import is_equal_unordered


def test_user(monkeypatch):

    def mock_get_users(*args):
        return [
            {
                'id': '1',
                'pseudo': 'Valentine',
                'email': 'VaLenTine@mail.fr'
            },
            {
                'id': '2',
                'pseudo': 'Tristan',
                'email': 'TRISTAN@MAIL.FR'
            }
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)
    user_service = UserService(user_fetcher_service=UserFetcherService())

    users = user_service.list_users()

    assert is_equal_unordered(users, [
        {
            'id': '1',
            'pseudo': 'Valentine',
            'email': 'valentine@mail.fr'
         },
        {
            'id': '2',
            'pseudo': 'Tristan',
            'email': 'tristan@mail.fr'
         }
    ])


def test_user_no_user(monkeypatch):

    def mock_get_users(*args):
        return []

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)
    user_service = UserService(user_fetcher_service=UserFetcherService())

    users = user_service.list_users()

    assert is_equal_unordered(users, [])

