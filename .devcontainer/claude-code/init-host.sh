#!/bin/sh
# Create the host directories that devcontainer.json bind-mounts.
# This script runs on the HOST before the container is created; docker refuses
# a bind mount whose source is missing, so a host without one cannot start it.
# mkdir -p is idempotent - it only creates if missing, won't clobber existing.

mkdir -p "$HOME/.claude" "$HOME/.config/gh"
