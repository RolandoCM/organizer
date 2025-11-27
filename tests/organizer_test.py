import os
from pathlib import Path

import pytest

try:
    # Prefer CLI invocation if the Typer app is exposed
    from typer.testing import CliRunner  # type: ignore
    from organizer.main import app  # type: ignore
    _USE_CLI = True
except Exception:
    # Fall back to calling functions directly
    from organizer.main import (  # type: ignore
        organize,
        organize_folders,
        organize_ends_with,
        organize_starts_with,
    )
    _USE_CLI = False


def _write(fname: Path):
    fname.write_text("test")


def _invoke(runner, args):
    return runner.invoke(app, args)


def test_organize_documents_moves_pdf(tmp_path):
    files_dir = tmp_path / "files"
    files_dir.mkdir()
    pdf = files_dir / "report.pdf"
    jpg = files_dir / "photo.jpg"
    _write(pdf)
    _write(jpg)

    if _USE_CLI:
        runner = CliRunner()
        result = _invoke(runner, ["organize", "documents", str(files_dir)])
        assert result.exit_code == 0, result.output
    else:
        # call function directly; signature in CLI expects (kind, path)
        organize("documents", str(files_dir))

    assert (files_dir / "Documents" / "report.pdf").exists()
    assert (files_dir / "photo.jpg").exists()


def test_organize_folders_moves_photos(tmp_path):
    files_dir = tmp_path / "files"
    files_dir.mkdir()
    a = files_dir / "a.jpg"
    b = files_dir / "b.png"
    c = files_dir / "c.txt"
    _write(a)
    _write(b)
    _write(c)

    if _USE_CLI:
        runner = CliRunner()
        result = _invoke(runner, ["organize-folders", str(files_dir)])
        assert result.exit_code == 0, result.output
    else:
        organize_folders(str(files_dir))

    assert (files_dir / "Photos" / "a.jpg").exists()
    assert (files_dir / "Photos" / "b.png").exists()
    assert (files_dir / "c.txt").exists()


def test_organize_ends_with_moves_matching_files(tmp_path):
    files_dir = tmp_path / "files"
    files_dir.mkdir()
    f1 = files_dir / "invoice_alex.pdf"
    f2 = files_dir / "note_alex.txt"
    f3 = files_dir / "other.pdf"
    _write(f1)
    _write(f2)
    _write(f3)

    if _USE_CLI:
        runner = CliRunner()
        result = _invoke(runner, ["organize-ends-with", str(files_dir), "alex"])
        assert result.exit_code == 0, result.output
    else:
        organize_ends_with(str(files_dir), "alex")

    target = files_dir / "EndsWith_alex"
    assert (target / "invoice_alex.pdf").exists()
    assert (target / "note_alex.txt").exists()
    assert (files_dir / "other.pdf").exists()


def test_organize_starts_with_moves_to_custom_target(tmp_path):
    files_dir = tmp_path / "files"
    files_dir.mkdir()
    f1 = files_dir / "factura_001.pdf"
    f2 = files_dir / "factura_002.pdf"
    f3 = files_dir / "other.pdf"
    _write(f1)
    _write(f2)
    _write(f3)

    if _USE_CLI:
        runner = CliRunner()
        result = _invoke(
            runner, ["organize-starts-with", str(files_dir), "Invoices", "factura"]
        )
        assert result.exit_code == 0, result.output
    else:
        organize_starts_with(str(files_dir), "Invoices", "factura")

    target = files_dir / "Invoices"
    assert (target / "factura_001.pdf").exists()
    assert (target / "factura_002.pdf").exists()
    assert (files_dir / "other.pdf").exists()