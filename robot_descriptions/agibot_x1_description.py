#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""AgiBot X1 description."""

from os import getenv as _getenv
from os import path as _path

from ._cache import clone_to_cache as _clone_to_cache

REPOSITORY_PATH: str = _clone_to_cache(
    "agibot_x1_description",
    commit=_getenv("ROBOT_DESCRIPTION_COMMIT", None),
)

PACKAGE_PATH: str = _path.join(REPOSITORY_PATH, "resources", "robots", "x1")

URDF_PATH: str = _path.join(PACKAGE_PATH, "urdf", "x1.urdf")
