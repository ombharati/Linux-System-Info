# Linux System Info

A small Python CLI utility that displays basic information about a Linux system.

## Features

- System information
- CPU core count
- Memory usage
- Disk usage
- System uptime

## Requirements

- Linux
- Python 3.x
- No external dependencies

## Usage

```bash
python3 system_info.py
```



See [ARCHITECTURE.md]([ARCHITECTURE.md](https://github.com/ombharati/Linux-System-Info/blob/main/ARCHITECTURE.md)) for the internal design and data flow.

## What I Learned

This project helped me understand how Python can interact with the underlying Linux system.

### Python

- Using the standard library for system-level tasks
- Working with modules such as `os`, `platform`, and `shutil`
- Reading files and parsing structured text
- Organizing functionality into small, reusable functions
- Using dictionaries to return structured data

### Linux

- Understanding the `/proc` virtual filesystem
- Reading memory information from `/proc/meminfo`
- Reading system uptime from `/proc/uptime`
- Understanding basic Linux system statistics
- Working with filesystem disk usage

### Git & Project Structure

- Creating a small project with a clear structure
- Using `.gitignore` for Python projects
- Writing documentation with Markdown
- Separating project architecture from general documentation

## Limitations

This is intentionally a simple project. It currently focuses on basic system information rather than detailed monitoring or real-time statistics.
