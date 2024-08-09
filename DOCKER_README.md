### lizardbyte/plexyglass

> **Attention**: Plex is removing ALL support for plugins. This project is no longer maintained.
> See [Plex Forum](https://forums.plex.tv/t/important-information-for-users-running-plex-media-server-on-nvidia-shield-devices/883484)
> for more information.

This is a [docker-mod](https://linuxserver.github.io/docker-mods/) for
[plex](https://hub.docker.com/r/linuxserver/plex) which adds [PlexyGlass](https://github.com/LizardByte/PlexyGlass)
to plex as a plugin, to be downloaded/updated during container start.

This image extends the plex image, and is not intended to be created as a separate container.

### Installation

In plex docker arguments, set an environment variable `DOCKER_MODS=lizardbyte/plexyglass:latest` or
`DOCKER_MODS=ghcr.io/lizardbyte/plexyglass:latest`

If adding multiple mods, enter them in an array separated by `|`, such as
`DOCKER_MODS=lizardbyte/plexyglass:latest|linuxserver/mods:other-plex-mod`

### Supported Architectures

Specifying `lizardbyte/plexyglass:latest` or `ghcr.io/lizardbyte/plexyglass:latest` should retrieve the correct image
for your architecture.

The architectures supported by this image are:

| Architecture | Available |
|:------------:|:---------:|
|    x86-64    |     ✅     |
|    arm64     |     ✅     |
|    armhf     |     ✅     |
