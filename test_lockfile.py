#!/usr/bin/env python3
"""Test script for pixi lockfile functionality."""

import os
import shutil
import subprocess
from pathlib import Path


def main() -> None:
    cache_dir = Path("pixi-cache").resolve()
    pixi_home = Path("pixi-global").resolve()

    # Clean directories
    if cache_dir.exists():
        shutil.rmtree(cache_dir)
    if pixi_home.exists():
        shutil.rmtree(pixi_home)

    # Run pixid global install
    print("Running pixid global install...")
    subprocess.run(
        ["pixi", "global", "install", "--path", "pixi-package"],
        env=os.environ
        | {"PIXI_HOME": str(pixi_home), "PIXI_CACHE_DIR": str(cache_dir)},
        check=True,
    )

    # Run pixid install
    print("Running pixid install...")
    subprocess.run(
        ["pixid", "install", "--environment", "source"],
        env=os.environ | {"PIXI_CACHE_DIR": str(cache_dir)},
        check=True,
    )


if __name__ == "__main__":
    main()
