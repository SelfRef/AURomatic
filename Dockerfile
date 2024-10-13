FROM archlinux:base-devel

RUN pacman -Sy devtools namcap nodejs yarn python python-fastapi

VOLUME /pkgbuilds

WORKDIR /pkgbuilds
