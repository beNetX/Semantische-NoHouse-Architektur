# SPDX-License-Identifier: LicenseRef-SinnZeit-1.0
# SPDX-FileCopyrightText: 2025 beNetX – Moritz Oliver Benatzky
# SPDX-Comment: An artifact of the NoHouse.DotMesh—born from the synthesis of human vision and machine logic.

from __future__ import annotations
from importlib import metadata

try:
    __version__ = metadata.version("benetx-public")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0-dev" 
