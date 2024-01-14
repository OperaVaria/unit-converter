
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2023.01.14

### Added

- A proper unit database in sqlite format.
- Uploaded the database content in a more accessible .csv format as well.
- Unit system information, carried in System objects, displayed in a widget.
- Added new unit systems (Pressburg area; Kőszeg, Sárvár, Tokay vineyard area; Buda length).
- Added a unittest script.
- Added warning messages if a module is launched as main accidentally.
- Added changelog.
- Added compiled releases.

### Changed

- Major code rationalization.
- Unit and System objects now built from database.
- The decimal module is now used for more precise calculations and simpler rounding.
- GUI resized to 1080p and launches maximized.
- Updated Sources.md file.
- Updated README.md file.

### Removed

- Old unit_list.py files.

### Fixed

- Typos and mistakes in the code and database.
- The result can now be copied.
- Issues with the ttk theme, mainly on Linux.
- Label texts' justification in Python version 3.12.

## [0.0.1] - 2023.12.17

### Added

- Initial release.
