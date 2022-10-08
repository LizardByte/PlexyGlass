# syntax = docker/dockerfile:latest
FROM python:2.7.18-buster AS buildstage

# build args
ARG BUILD_VERSION
ARG COMMIT
ARG GITHUB_SHA=$COMMIT
# note: BUILD_VERSION may be blank, COMMIT is also available
# note: build_plist.py uses BUILD_VERSION and GITHUB_SHA

# create build dir and copy GitHub repo there
# todo - add `--link` once hadolint supports this syntax, see https://github.com/hadolint/hadolint/issues/826
COPY . /build

# set build dir
WORKDIR /build

# test, list files including hidden ones - todo - remove this
RUN ls -a

# update packages
RUN apt-get update  \
    && apt-get -y --no-install-recommends install \
      # install git -> required for pip to install from git
      git=1:2.20.1* \
    && rm -rf /var/lib/apt/lists/*

# install build requirements
RUN python -m pip --no-python-version-warning --disable-pip-version-check install --no-cache-dir --upgrade \
      pip==20.3.4 setuptools \
    && python -m pip install --no-cache-dir --upgrade -r requirements-dev.txt

# build plugin
RUN python ./scripts/install_requirements.py \
    && python ./scripts/build_plist.py \

# clean
RUN rm -rf ./scripts/

FROM scratch AS deploy

# variables
ARG PLUGIN_NAME="PlexyGlass.bundle"
ARG PLUGIN_DIR="/config/Library/Application Support/Plex Media Server/Plug-ins"

# add files from buildstage
# todo - add `--link` once hadolint supports this syntax, see https://github.com/hadolint/hadolint/issues/826
COPY --from=buildstage /build/ $PLUGIN_DIR/$PLUGIN_NAME
