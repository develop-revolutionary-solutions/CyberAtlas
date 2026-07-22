# HTB Assistant Architecture

```
User

↓

CLI

↓

Command Dispatcher

↓

Modules

Workspace
Identify
Hash
Strings
Decode
ELF
PE
PCAP
Web
OSINT

↓

Output Formatter

↓

Notes
```

---

Design Goals

- Small
- Fast
- Offline
- CPU Friendly
- Modular
- Testable



assistant/
├── cli/
│   ├── doctor.py
│   ├── inspect.py
│   ├── workspace.py
│   └── decode.py
│
└── modules/
    ├── doctor/
    ├── inspect/
    ├── workspace/
    └── decode/



