:github_url: https://github.com/LizardByte/PlexyGlass/tree/nightly/docs/source/about/usage.rst

Usage
=====

End Users
---------
Minimal setup is required to use PlexyGlass. In addition to the installation, a couple of settings may be configured.

   #. Navigate to the `Plugins` menu within the Plex server settings.
   #. Select the gear cog when hovering over the PlexyGlass plugin tile.
   #. Set the values of the preferences and save.

      .. Warning:: Plex stores configuration values in the log. If you upload your logs for support, it would be wise to
         review the data in the log file.

Developers
----------
This section is intended for developers utilizing the plugin to support URL services or the like.

It is very easy to use the URL service in your metadata agent. Below is an example.

.. code-block:: python

   video_title='Rick Astley - Never Gonna Give You Up (Official Music Video)'
   video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'

   metadata.extras.add(OtherObject(title=video_title, url=video_url))

You can pass in many other parameters if you'd like, but they are all optional except the url. Below is a bare
minimal example.

.. code-block:: python

   video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'

   metadata.extras.add(OtherObject(url=video_url))

.. Tip:: For help with metadata agent or general plug-in development, check out our
   `plexhints <https://app.lizardbyte.dev/#Projects>`_ python library.
