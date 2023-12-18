:github_url: https://github.com/LizardByte/PlexyGlass/blob/master/docs/source/contributing/build.rst

Build
=====
Compiling PlexyGlass is fairly simple; however it is recommended to use Python 2.7 since the Plex framework is using
Python 2.7.

Clone
-----
Ensure `git <https://git-scm.com/>`__ is installed and run the following:

   .. code-block:: bash

      git clone --recurse-submodules https://github.com/lizardbyte/plexyglass.git plexyglass.bundle
      cd ./plexyglass.bundle

Setup venv
----------
It is recommended to setup and activate a `venv`_.

Apply Patches
-------------
Patch YouTube-DL
   .. code-block:: bash

      pushd ./third-party/youtube-dl
      git apply -v ../../patches/youtube_dl-compat.patch
      popd

Install Requirements
--------------------
Install Requirements
   .. code-block:: bash

      python -m pip install --upgrade --target=./Contents/Libraries/Shared -r requirements.txt --no-warn-script-location

Development Requirements
   .. code-block:: bash

      python -m pip install -r requirements-dev.txt

Build Plist
-----------
   .. code-block:: bash

      python ./scripts/build_plist.py

Remote Build
------------
It may be beneficial to build remotely in some cases. This will enable easier building on different operating systems.

#. Fork the project
#. Activate workflows
#. Trigger the `CI` workflow manually
#. Download the artifacts from the workflow run summary

.. _venv: https://docs.python.org/3/library/venv.html
