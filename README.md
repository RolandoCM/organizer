// ...existing code...
# organizer

Simple CLI utilities to organize files in a folder (photos, documents, and name-based grouping).

## Project files
- `organizer/main.py` — main CLI implementation (Typer app).
- `pyproject.toml` — project metadata and dependencies.
- `.gitignore` — ignores the `files/` test data folder.
- `files/` — example files used for manual testing.

## Commands (implemented in `organizer/main.py`)
- `organizer.main.organize` — move documents or photos into subfolders.
- `organizer.main.organize_folders` — organize files into `Photos` (by extension).
- `organizer.main.organize_with_pattern` — placeholder for pattern-based organization.
- `organizer.main.organize_ends_with` — move files whose basename ends with a suffix.
- `organizer.main.organize_starts_with` — move files whose name starts with a prefix.

## Installation
Ensure Python 3.12+ is installed. Install Typer (specified in `pyproject.toml`) or create a virtual environment:

```sh
python -m venv .venv
.venv/bin/pip install -r <(echo "typer==0.20.0")
```

Or install via Poetry if you use it:

```sh
poetry install
```

## Usage examples
Run the CLI module directly:

```sh
python -m organizer.main organize documents files/
```

Example commands:
- Move documents from `files/` into `files/Documents/`:

```sh
python -m organizer.main organize documents files/
```

- Organize photos into `files/Photos/`:

```sh
python -m organizer.main organize_folders files/
```

- Move files whose base name ends with `alex` into `files/EndsWith_alex/`:

```sh
python -m organizer.main organize_ends_with files/ alex
```

- Move files starting with `factura` into a custom target folder:

```sh
python -m organizer.main organize_starts_with files/ Invoices factura
```

## Notes and TODOs
- The CLI is implemented using Typer in `organizer/main.py`. The commands contain basic moving logic for demonstration and need improved error handling, a dry-run option, and unit tests.
- Add tests under `tests/` to cover file movement behaviors.

## License
MIT License
