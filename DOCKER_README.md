# Docker

This is a docker mod for Plex which adds [PlexyGlass](https://github.com/LizardByte/PlexyGlass) to Plex as a plugin,
to be downloaded/updated during container start.

In plex docker arguments, set an environment variable `DOCKER_MODS=lizardbyte/plexyglass:latest`

If adding multiple mods, enter them in an array separated by `|`, such as
`DOCKER_MODS=lizardbyte/plexyglass:latest|linuxserver/mods:other-plex-mod`

For more information about linuxserver docker-mods, see [here](https://linuxserver.github.io/docker-mods/).
