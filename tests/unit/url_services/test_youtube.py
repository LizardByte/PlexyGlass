# -*- coding: utf-8 -*-

# lib imports
import pytest


@pytest.fixture(scope='module')
def service(service_url_youtube):
    yield service_url_youtube


@pytest.fixture(scope='module', params=[
    'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    'https://youtube.com/watch?v=dQw4w9WgXcQ',
    'https://youtu.be/dQw4w9WgXcQ',
])
def url_list_1(request):
    yield request.param


# only use this for normalize because the playlist takes a long time to process
@pytest.fixture(scope='module', params=[
    'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    'https://youtube.com/watch?v=dQw4w9WgXcQ',
    'https://youtu.be/dQw4w9WgXcQ',
    'https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1'  # mix
])
def url_list_2(request):
    yield request.param


def test_extract_youtube_data(service, url_list_1):
    assert service.extract_youtube_data(url=url_list_1)


def test_normalize_url(service, url_list_2):
    uut = service.NormalizeURL(url=url_list_2)
    assert uut
    assert uut == 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


def test_metadata_object_for_url(service, url_list_1):
    uut = service.MetadataObjectForURL(url=url_list_1)
    assert uut
    # todo - plexhints needs to be improved in order to test this properly


def test_media_objects_for_url(service, url_list_1):
    uut = service.MediaObjectsForURL(url=url_list_1)
    assert uut
    assert isinstance(uut, list)
    assert len(uut) > 0

    for media in uut:
        assert media
        # todo - plexhints needs to be improved in order to test this properly
