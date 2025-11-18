import pytest


@pytest.fixture(autouse=True)
def _skipAll() -> None:
    """Skips all pytest ddfdstests in this directory."""
    pytest.skip(reason="Excluded from testing.")
