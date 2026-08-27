# Linux System Info

A simple Python utility for displaying basic system information on Linux.

## Features

- Operating system and kernel release
- System architecture
- Hostname
- CPU core count
- Memory usage
- Disk usage
- System uptime

The script uses only Python's standard library and Linux's `/proc` filesystem.

## Requirements

- Linux
- Python 3.x

No external dependencies are required.

## Usage

Clone the repository:

```bash
git clone https://github.com/ombharati/linux-system-info.git
cd linux-system-info
```

Run the script:

```bash
python3 system_info.py
```

## Example Output

```text
=============================================
             LINUX SYSTEM INFO
=============================================

[ SYSTEM ]
OS:           Linux
Release:      6.8.0
Architecture: x86_64
Hostname:     linux-machine

[ CPU ]
CPU cores:    8

[ MEMORY ]
Total:        15892 MB
Used:         6234 MB
Available:    9658 MB

[ DISK ]
Total:        475.8 GB
Used:         183.4 GB
Free:         292.4 GB

[ UPTIME ]
Uptime:       12h 37m

=============================================
```

## How It Works

### System Information

The `platform` module provides the operating system, kernel release, architecture, and hostname.

### CPU

The `os.cpu_count()` function returns the number of available CPU cores.

### Memory

Memory statistics are read from:

```text
/proc/meminfo
```

The script uses `MemTotal` and `MemAvailable` to calculate memory usage:

```text
Used = Total - Available
```

### Disk

Disk usage is obtained using:

```python
shutil.disk_usage("/")
```

This reports the total, used, and free space on the root filesystem.

### Uptime

System uptime is read from:

```text
/proc/uptime
```

The uptime is converted from seconds into hours and minutes.

## Project Structure

```text
linux-system-info/
├── system_info.py
└── README.md
```

## Limitations

- Linux only
- Memory information depends on `/proc/meminfo`
- Uptime depends on `/proc/uptime`
- Disk information currently covers only `/`
- CPU information is limited to the number of cores

## License

This project is open source. Add a license file if you intend to distribute the project publicly.
