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





# Changelog

## v0.3.0-dev

### Added

#### Decode Module

- Implemented Decode CLI.
- Added automatic detection for:
  - Base64
  - Binary
  - Hex
  - URL Encoding
  - Base32
  - Base85
- Improved decode error handling using Rich panels.
- Added Decode unit tests.
- 7/7 Decode tests passing.

#### ELF Module

- Implemented ELF analysis service.
- Implemented ELF CLI.
- Added support for:
  - ELF Class
  - Architecture
  - Endianness
  - Entry Point
  - Interpreter
  - PIE Detection
  - NX Detection
  - RELRO Detection
  - Stack Canary Detection
  - Stripped Detection
- Added ELF unit tests.
- ELF analysis verified against system binaries.
- 1/1 ELF tests passing.

### Fixed

- Binary decoding incorrectly detected as Hex.
- Base85 shell quoting documentation.
- Removed automatic ROT13 detection to prevent false positives.
- Improved Decode CLI error presentation.

---

## Current Test Status

Passing

- Decode: 7
- ELF: 1

Total

8 Passing Tests

---

Next

- PE Module
- PCAP Module
- Web Module
- Rules Module




## v0.5.0-dev

### Added

PE Module

- PE Analyzer
- PE CLI
- ASLR detection
- DEP detection
- Section parsing
- Import parsing
- PE unit tests

PCAP Module

- PCAP Analyzer
- PCAP CLI
- Packet counting
- Protocol detection
- DNS extraction
- HTTP host extraction
- HTTP URI extraction
- IPv4 extraction
- PCAP unit tests

### Testing

28 tests passing




