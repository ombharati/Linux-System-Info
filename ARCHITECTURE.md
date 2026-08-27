# Architecture

## Overview

Linux System Info is a small Python CLI utility with a simple functional architecture. It collects system information from Python's standard library and Linux's `/proc` filesystem, then formats and prints the results to the terminal.

```text
                    ┌─────────────────────┐
                    │        main()       │
                    │   Application Flow  │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
 ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
 │ get_os_info()   │  │ get_cpu_info()  │  │get_memory_info()│
 └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
          │                    │                    │
          ▼                    ▼                    ▼
     platform module       os module        /proc/meminfo
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ get_disk_info()     │
                    │ shutil.disk_usage() │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ get_uptime()        │
                    │ /proc/uptime        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Terminal Output     │
                    └─────────────────────┘
```

## Components

### `main()`

The entry point and orchestration layer.

Responsibilities:

1. Call each information-gathering function.
2. Store the returned data.
3. Format the information.
4. Print the final output.

`main()` does not directly interact with `/proc` or system APIs.

### `get_os_info()`

Collects general system information using Python's `platform` module.

Returns:

```text
OS
Release
Architecture
Hostname
```

### `get_cpu_info()`

Collects CPU information using the `os` module.

Returns:

```text
CPU cores
```

### `get_memory_info()`

Reads Linux memory statistics from:

```text
/proc/meminfo
```

It extracts `MemTotal` and `MemAvailable`, then calculates:

```text
Used = Total - Available
```

### `get_disk_info()`

Uses `shutil.disk_usage("/")` to retrieve storage information for the root filesystem.

Returns:

```text
Total
Used
Free
```

### `get_uptime()`

Reads system uptime from:

```text
/proc/uptime
```

The value is converted from seconds into hours and minutes.

## Data Flow

```text
Linux System
     │
     ├── platform
     ├── os
     ├── /proc/meminfo
     ├── shutil
     └── /proc/uptime
             │
             ▼
     Information Functions
             │
             ▼
        Python dictionaries
             │
             ▼
           main()
             │
             ▼
      Formatted terminal output
```

## Design

The project follows a simple separation of responsibilities:

| Component | Responsibility |
|---|---|
| `get_os_info()` | Operating system information |
| `get_cpu_info()` | CPU core information |
| `get_memory_info()` | Memory statistics |
| `get_disk_info()` | Disk statistics |
| `get_uptime()` | System uptime |
| `main()` | Orchestration and presentation |

Each information function is independent and returns structured data rather than printing directly.

## Dependencies

The project has no third-party dependencies.

```text
Python Standard Library
├── os
├── platform
└── shutil

Linux
└── /proc
    ├── meminfo
    └── uptime
```

## Execution Flow

```text
Program starts
      │
      ▼
if __name__ == "__main__"
      │
      ▼
    main()
      │
      ├── get_os_info()
      ├── get_cpu_info()
      ├── get_memory_info()
      ├── get_disk_info()
      └── get_uptime()
      │
      ▼
Format collected information
      │
      ▼
Print to terminal
      │
      ▼
Program exits
```

## Project Structure

```text
linux-system-info/
├── system_info.py
├── README.md
├── ARCHITECTURE.md
└── .gitignore
```

## Future Expansion

The current architecture can be extended by adding independent information functions without significantly changing `main()`.

Potential additions include:

- CPU model and frequency
- CPU utilization
- Network interfaces
- IP addresses
- Logged-in users
- Process information
- GPU information
- Temperature sensors
- Individual filesystem usage

Each new feature can follow the existing pattern:

```text
System Data
    │
    ▼
Information Function
    │
    ▼
Structured Result
    │
    ▼
main()
    │
    ▼
Terminal Output
```
