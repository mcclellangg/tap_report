# tests/test_assets.py

"""
Tests created with Gemini.
Gemini Session: https://share.gemini.google/ejQPJJpt0fwQ
"""

import re
from pathlib import Path
import pytest
from app import app


@pytest.fixture
def client():
    """Configures the Flask test client using your global app instance."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_rendered_page_links_load(client):
    """Render the index page, extract all static links, and verify they load successfully."""
    response = client.get("/")
    assert response.status_code == 200

    html_content = response.get_data(as_text=True)

    # Find all href and src attributes pointing to static assets
    static_links = re.findall(r'(?:href|src)=["\'](/static/[^"\']+)["\']', html_content)
    static_links = list(set(static_links))

    assert len(static_links) > 0, "No static assets found in rendered index.html!"

    for link in static_links:
        asset_response = client.get(link)
        assert asset_response.status_code == 200, (
            f"Broken link in template: {link} returned status {asset_response.status_code}"
        )


def test_no_hardcoded_absolute_static_paths():
    """Assert that templates do not use raw absolute paths like src='/static/...'."""
    template_path = Path("templates") / "index.html"
    if template_path.exists():
        content = template_path.read_text(encoding="utf-8")

        hardcoded_matches = re.findall(
            r'<script[^>]+src=["\']/static/[^"\']*["\']', content
        )
        assert not hardcoded_matches, (
            f"Found hardcoded static script path in {template_path}: {hardcoded_matches}. "
            "Use url_for('static', filename='...') instead!"
        )
