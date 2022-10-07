# buildstage
FROM python:2.7.18-buster as buildstage

# build args
ARG BUILD_VERSION
ARG COMMIT
ARG GITHUB_SHA=$COMMIT
# note: BUILD_VERSION may be blank, COMMIT is also available
# note: build_plist.py uses BUILD_VERSION and GITHUB_SHA

# setup build directory
RUN mkdir /build
WORKDIR /build/

# copy repo
COPY . .

RUN \
    # update Alpine packages
    apt-get update && apt-get -y --no-install-recommends install \
      # install git -> required for pip to install from git
      git=1:2.20.1* \
    && rm -rf /var/lib/apt/lists/* \
    # update python/pip
    && python -m pip --no-python-version-warning --disable-pip-version-check install --no-cache-dir --upgrade \
      pip==20.3.4 setuptools \
    # install build requirements
    && python -m pip install --no-cache-dir --upgrade -r requirements-dev.txt \
    # install plugin requirements
    && python ./scripts/install_requirements.py \
    # build plist file
    && python ./scripts/build_plist.py \
    # remove scripts directory
    && rm -rf ./scripts/

# single layer deployed image
FROM scratch

# variables
ARG PLUGIN_NAME="PlexyGlass.bundle"
ARG PLUGIN_DIR="/config/Library/Application Support/Plex Media Server/Plug-ins"

# add files from buildstage
COPY --from=buildstage /build/ $PLUGIN_DIR/$PLUGIN_NAME
