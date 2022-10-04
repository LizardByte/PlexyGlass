# -*- coding: utf-8 -*-

# standard imports
import sys

# plex debugging
if 'plexscripthost' not in sys.executable.lower() or sys.executable != '':  # the code is running outside of Plex
    from plexhints import plexhints_setup, update_sys_path
    plexhints_setup()  # read the plugin plist file and determine if plexhints should use elevated policy or not
    update_sys_path()  # when running outside plex, append the path

    from plexhints.decorator_kit import handler  # decorator kit
    from plexhints.log_kit import Log  # log kit
    from plexhints.object_kit import MessageContainer  # object kit
    from plexhints.prefs_kit import Prefs  # prefs kit

# local imports
if sys.version_info.major < 3:
    from default_prefs import default_prefs
else:
    from .default_prefs import default_prefs


def validate_prefs():
    # type: () -> MessageContainer
    """
    Validate plug-in preferences.

    This function is called when the user modifies their preferences. The developer can check the newly provided values
    to ensure they are correct (e.g. attempting a login to validate a username and password), and optionally return a
    ``MessageContainer`` to display any error information to the user. See the archived Plex documentation
    `Predefined functions
    <https://web.archive.org/web/https://dev.plexapp.com/docs/channels/basics.html#predefined-functions>`_
    for more information.

    Returns
    -------
    MessageContainer
        Success or Error message dependeing on results of validation.

    Examples
    --------
    >>> validate_prefs()
    ...
    """
    # todo - validate values are proper type of data, same as retroarcher
    # todo - validate username and password
    #  does this ``Code`` have visibility of the ServicePrefs.json options? ... probably yes

    error_message = ''  # start with a blank error message

    for key in default_prefs:
        try:
            Prefs[key]
        except KeyError:
            Log.Critical("Setting '%s' missing from 'DefaultPrefs.json'" % key)
            error_message += "Setting '%s' missing from 'DefaultPrefs.json'<br/>" % key
        else:
            # test all types except 'str_' as string cannot fail
            if key.startswith('int_'):
                try:
                    int(Prefs[key])
                except ValueError:
                    Log.Error("Setting '%s' must be an integer; Value '%s'" % (key, Prefs[key]))
                    error_message += "Setting '%s' must be an integer; Value '%s'<br/>" % (key, Prefs[key])
            elif key.startswith('bool_'):
                if Prefs[key] is not True and Prefs[key] is not False:
                    Log.Error("Setting '%s' must be True or False; Value '%s'" % (key, Prefs[key]))
                    error_message += "Setting '%s' must be True or False; Value '%s'<br/>" % (key, Prefs[key])

    if error_message != '':
        return MessageContainer(header='Error', message=error_message)
    else:
        Log.Info("DefaultPrefs.json is valid")
        return MessageContainer(header='Success', message='RetroArcher - Provided preference values are ok')


def start():
    # type: () -> None
    """
    Start the plug-in.

    This function is called when the plug-in first starts. It can be used to perform extra initialisation tasks such as
    configuring the environment and setting default attributes. See the archived Plex documentation
    `Predefined functions
    <https://web.archive.org/web/https://dev.plexapp.com/docs/channels/basics.html#predefined-functions>`_
    for more information.

    Examples
    --------
    >>> start()
    ...
    """
    # validate prefs
    prefs_valid = validate_prefs()
    if prefs_valid.header == 'Error':
        Log.Warn('PlexyGlass plug-in preferences are not valid.')

    Log.Debug('PlexyGlass plug-in started.')


@handler(prefix='/video/plexyglass', name='PlexyGlass', thumb='attribution.png')
def main():
    """
    Create the main plug-in ``handler``.

    This is responsible for displaying the plug-in in the plug-ins menu. Since we are using the ``@handler`` decorator,
    and since Plex removed menu's from plug-ins, this method does not need to perform any other function.
    """
    pass


# remap plex predefined functions... function names should be lowercase
Start = start
ValidatePrefs = validate_prefs
