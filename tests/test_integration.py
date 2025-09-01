import pytest, subprocess
from pathlib import Path

program = str(Path(__file__).parents[1].absolute() / "application.bat")

@pytest.mark.integration
def test_cli_math_add():
    out = subprocess.check_output([program, "math", "add", "2", "3"], text=True, shell=True)
    assert out.strip() == "5.0"


@pytest.mark.integration
def test_cli_string_slugify():
    out = subprocess.check_output([program, "string", "slugify", "Hello World"], text=True, shell=True)
    assert out.strip() == "hello-world"
