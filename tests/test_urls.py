import pytest

from unittest import mock
from src.deadlinkz import checkLinks, checkSingleLink


def mock_200_requests_get():
    return {200}


def mock_404_requests_get():
    return {404}


def test_200_multiple_no_mock():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        links = ["https://www.youtube.com/", "https://www.youtube.com/watch?v=oHg5SJYRHA0", "https://github.com/"]
        checkLinks(links)
    assert pytest_wrapped_e.value.code == 0


def test_404_multiple_no_mock():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        links = ["https://www.youtube.com/erduhbwejkbwehjb", "https://gbatemp.net/hi", "https://github.com/6sbm29,"]
        checkLinks(links)
    assert pytest_wrapped_e.value.code == 1


@mock.patch('src.deadlinkz.requests.head', side_effect=mock_200_requests_get())
def test_200_single_mock(self):
    r = checkSingleLink('http://google.com/')
    assert r == 200


@mock.patch('src.deadlinkz.requests.head', side_effect=mock_404_requests_get())
def test_404_single_mock(self):
    r = checkSingleLink('http://google.com/')
    assert r == 404




