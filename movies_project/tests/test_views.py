from unittest.mock import Mock
from urllib.parse import quote

import pytest
from main import app
from tmdb_client import get_available_list_types

available_list_types = get_available_list_types()

@pytest.mark.parametrize(
    'list_type, status_code',
    tuple((i, 200) for i in available_list_types))
def test_homepage(monkeypatch, list_type, status_code):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get(f'/?list_type={quote(list_type)}')
       assert response.status_code == status_code
       api_mock.assert_called_once_with(f'movie/{list_type}')
