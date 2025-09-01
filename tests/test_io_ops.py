import pytest, subprocess
from pathlib import Path

program = str(Path(__file__).parents[1].absolute() / "application.bat")


@pytest.mark.io
def test_write_and_read_text(tmp_path: Path):
    p = tmp_path / "note.txt"
    subprocess.run([program, "io", "write-text", p, "hello"], text=True, shell=True)
    out = subprocess.check_output([program, "io", "read-text", p], text=True, shell=True)
    assert out == "hello\n"

@pytest.mark.io
def test_count_lines(tmp_path: Path):
    p = tmp_path / "file.txt"
    subprocess.run([program, "io", "write-text", p, "a\n\nccc\n"], text=True, shell=True)
    out = subprocess.check_output([program, "io", "count-lines", p], text=True, shell=True)
    assert int(out) > 0
