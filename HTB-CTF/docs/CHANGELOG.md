# Changelog

## v0.1.0-dev

Initial HTB branch.

Added

- Documentation
- Sprint Planning

---

Future

### Added

### Changed

### Fixed

### Removed



# Changelog

## v0.2.0-dev

### Added

Doctor Command

- Python Version Check
- Operating System Check
- Workspace Validation
- Tool Detection

Verified

- file
- strings
- readelf
- objdump
- checksec
- tshark
- curl
- wget
- nmap
- ffuf
- gobuster
- binwalk
- exiftool
- steghide
- john
- hashcat
- sqlmap
- yara
- radare2
- gdb

Result

20/20 tools detected successfully.

---

### In Progress

Inspect Module

Completed

- Service Layer
- File Type Detection
- Hashes
- Entropy
- URL Detection
- Email Detection
- IP Detection
- Flag Detection
- Recommendation Engine

Remaining

- CLI
- Tests





## v0.1.0-dev

### Added

- Implemented Inspect service.
- Implemented Inspect CLI.
- Added file triage:
  - hashes
  - entropy
  - URLs
  - emails
  - IPv4
  - flag extraction
  - recommendations

- Implemented Workspace service.
- Implemented Workspace CLI.
- Automatic HTB workspace creation.
- README.md generation.
- writeup.md generation.
- Improved idempotent workspace handling.

- Started Decode module.
- Implemented Decoder service.
- Added support for:
  - Base64
  - Hex
  - URL
  - Binary
  - Base32
  - Base85
  - ROT13





