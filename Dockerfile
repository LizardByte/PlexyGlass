# syntax=docker/dockerfile:1.4
# artifacts: false
# platforms: linux/amd64,linux/arm64/v8,linux/arm/v7
FROM ubuntu:24.04 AS buildstage

# build args
ARG BUILD_VERSION
ARG COMMIT
ARG GITHUB_SHA=$COMMIT
# note: BUILD_VERSION may be blank, COMMIT is also available
# note: build_plist.py uses BUILD_VERSION and GITHUB_SHA

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# install dependencies
RUN <<_DEPS
#!/bin/bash
set -e
apt-get update -y
apt-get install -y --no-install-recommends \
  patch \
  python2=2.7.18* \
  python-pip=20.3.4*
apt-get clean
rm -rf /var/lib/apt/lists/*
_DEPS

# create build dir and copy GitHub repo there
COPY --link . /build

# set build dir
WORKDIR /build

# update pip
RUN <<_PIP
#!/bin/bash
set -e
python2 -m pip --no-python-version-warning --disable-pip-version-check install --no-cache-dir --upgrade \
  pip setuptools
# dev requirements not necessary for docker image, significantly speeds up build since lxml doesn't need to build
_PIP

# build plugin
RUN <<_BUILD
#!/bin/bash
set -e
python2 -m pip --no-python-version-warning --disable-pip-version-check install --no-cache-dir --upgrade \
  --target=./Contents/Libraries/Shared -r requirements.txt --no-warn-script-location
python2 ./scripts/build_plist.py
_BUILD

## patch youtube-dl, cannot use git apply because we don't pass in any git files
#WORKDIR /build/Contents/Libraries/Shared
#RUN <<_PATCH
##!/bin/bash
#set -e
#patch_dir=/build/patches
#patch -p1 < "${patch_dir}/youtube_dl-compat.patch"
#_PATCH

WORKDIR /build

# clean
RUN <<_CLEAN
#!/bin/bash
set -e
rm -rf ./scripts/
# list contents
ls -a
_CLEAN

FROM scratch AS deploy

# variables
ARG PLUGIN_NAME="PlexyGlass.bundle"
ARG PLUGIN_DIR="/config/Library/Application Support/Plex Media Server/Plug-ins"

# add files from buildstage
COPY --link --from=buildstage /build/ $PLUGIN_DIR/$PLUGIN_NAME
