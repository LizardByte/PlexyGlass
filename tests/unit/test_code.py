# -*- coding: utf-8 -*-

# lib imports
from plexhints.object_kit import MessageContainer

# local imports
from Code import Start
from Code import ValidatePrefs
from Code import default_prefs


def test_validate_prefs():
    result_container = ValidatePrefs()
    assert isinstance(result_container, MessageContainer)
    assert result_container.header == "Success"
    assert "Provided preference values are ok" in result_container.message

    # invalidate prefs, cannot do this due to:
    # TypeError: '_PreferenceSet' object does not support item assignment
    # Code.Prefs['int_plexapi_plexapi_timeout'] = 'not an integer'
    # result_container = ValidatePrefs()
    # assert isinstance(result_container, MessageContainer)
    # assert result_container.header == "Error"
    # assert "must be an integer" in result_container.message


def test_validate_prefs_default_prefs():
    # add a default pref and make sure it is not in DefaultPrefs.json
    default_prefs['new_pref'] = 'new_value'
    result_container = ValidatePrefs()
    assert isinstance(result_container, MessageContainer)
    assert result_container.header == "Error"
    assert "missing from 'DefaultPrefs.json'" in result_container.message


def test_start():
    # just run the function
    Start()


def test_main():
    # todo
    pass
