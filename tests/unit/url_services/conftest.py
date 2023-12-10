# -*- coding: utf-8 -*-

# standard imports
import imp
import os

# lib imports
import pytest

# get Services directories
services_dir = url_services_dir = os.path.join(pytest.contents_dir, 'Services')
url_dir = os.path.join(services_dir, 'URL')

service_file = 'ServiceCode.pys'


@pytest.fixture(scope='module')
def service_url_youtube():
    # type: () -> object

    # we need to use imp.load_source() to import the service code because it is not a standard python module
    name = 'YouTube'
    _name = 'service_url_{}'.format(name.lower())
    service = imp.load_source(_name, os.path.join(url_dir, name, service_file))
    return service
