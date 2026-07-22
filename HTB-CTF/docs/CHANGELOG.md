# Changelog

All notable changes to the CyberAtlas HTB Toolkit are documented in this file.

The project follows an incremental implementation workflow where every module must successfully pass:

- `python -m compileall assistant`
- `pytest`

before proceeding to the next module.

---

# v0.6.0-dev

## Added

### Web Module

Implemented the Web analysis module.

Features

- HTTP/HTTPS URL support
- Automatic URL normalization
- HTTP header collection
- HTTP status code detection
- Content-Type detection
- Cookie collection
- Cookie attribute parsing
  - Name
  - Domain
  - Path
  - Secure
  - HttpOnly
  - Expires
- robots.txt retrieval
- Graceful timeout handling
- Graceful connection error handling
- Rich CLI output

### Web CLI

Added

```text
cyberatlas web <url>
```

Displays

- Summary
- Status Code
- Content Type
- Cookie Count
- HTTP Headers
- Cookies
- robots.txt

### Testing

Implemented

- Local HTTP server testing
- robots.txt validation
- Cookie validation
- Header validation
- Offline deterministic testing

Result

```
29 / 29 tests passing
```

### Manual Validation

Successfully tested against

- example.com
- httpbin.org
- google.com
- hackthebox.com

Verified

- HTTP Headers
- Cookies
- robots.txt
- HTTPS support
- Cloudflare sites
- Redirect handling

---

# v0.5.0-dev

## Added

### PE Module

Implemented

- PE Analyzer
- PE CLI
- DOS Header parsing
- Machine detection
- Import Table parsing
- Section parsing
- ASLR detection
- DEP detection

Testing

- PE unit tests

### PCAP Module

Implemented

- PCAP Analyzer
- PCAP CLI
- Packet counting
- Protocol detection
- IPv4 extraction
- DNS extraction
- HTTP Host extraction
- HTTP URI extraction

Testing

- PCAP unit tests

---

# v0.4.0-dev

## Added

### Decode Module

Implemented

- Decode Service
- Decode CLI

Supported

- Base64
- Base32
- Base85
- Binary
- Hex
- URL Encoding
- ROT13

### ELF Module

Implemented

- ELF Analyzer
- ELF CLI

Features

- ELF Class
- Architecture
- Entry Point
- Endianness
- PIE
- NX
- RELRO
- Stack Canary
- Interpreter
- Stripped Detection

Testing

- Decode tests
- ELF tests

---

# v0.3.0-dev

## Added

### Workspace Module

Implemented

- Workspace creation
- HTB directory structure
- README generation
- writeup.md generation
- Idempotent workspace creation

### Inspect Module

Implemented

- File identification
- SHA256
- MD5
- SHA1
- Entropy calculation
- URL extraction
- Email extraction
- IPv4 extraction
- Flag detection
- Investigation recommendations

---

# v0.2.0-dev

## Added

### Doctor Module

Implemented

System diagnostics

Checks

- Python version
- Operating System
- Workspace
- Tool availability

Verified tools

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

Verification Result

```
20 / 20 tools detected
```

---

# v0.1.0-dev

## Initial Project

Created

- HTB branch
- Documentation
- Project structure
- Configuration system
- Config Manager
- Config Validator
- Logging framework
- CLI framework
- Testing framework

Implemented

- Doctor
- Inspect
- Workspace
- Decode
- ELF
- PE
- PCAP
- Web

---

# Current Project Status

## Modules

Completed

- Doctor
- Inspect
- Workspace
- Decode
- ELF
- PE
- PCAP
- Web

Next

- Crypto
- Networking
- Linux
- Forensics
- Reverse Engineering Enhancements

---

# Quality Gate

Current Status

```
python -m compileall assistant
PASS

pytest
29 / 29 PASSING
```
