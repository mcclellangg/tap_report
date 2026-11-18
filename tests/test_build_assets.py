# tests/test_build_assets.py

"""
Tests created with Claude.
Claude Session: https://claude.ai/share/f776fc5e-7bff-4104-9bc6-b9778800f6aa
"""

from pathlib import Path

import pytest

BUILD = Path(__file__).resolve().parent.parent / "build"


@pytest.mark.parametrize("asset", ["base.css", "colors.css", "script.js"])
def test_asset_is_built_and_linked(asset):
    # HACK: plain string search that assets exist on html. Do something better to test that they are imported and work.
    html = (BUILD / "index.html").read_text(encoding="utf-8")

    assert f"static/{asset}" in html, f"index.html doesn't reference {asset}"
    assert (BUILD / "static" / asset).is_file(), f"{asset} missing from build/static"
