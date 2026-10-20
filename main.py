import os
import platform
import shutil


def get_os_info():
    return {
        "OS": platform.system(),
        "Release": platform.release(),
        "Architecture": platform.machine(),
        "Hostname": platform.node(),
    }


def get_cpu_info():
    return {
        "CPU cores": os.cpu_count(),
    }


def get_memory_info():
    memory = {}

    with open("/proc/meminfo", "r") as file:
        for line in file:
            key, value = line.split(":", 1)
            value = int(value.strip().split()[0])
            memory[key] = value

    total = memory["MemTotal"]
    available = memory["MemAvailable"]
    used = total - available

    return {
        "Total": total,
        "Used": used,
        "Available": available,
    }


def get_disk_info():
    total, used, free = shutil.disk_usage("/")

    return {
        "Total": total,
        "Used": used,
        "Free": free,
    }


def get_uptime():
    with open("/proc/uptime", "r") as file:
        seconds = float(file.readline().split()[0])

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)

    return f"{hours}h {minutes}m"


def main():
    os_info = get_os_info()
    cpu_info = get_cpu_info()
    memory = get_memory_info()
    disk = get_disk_info()
    uptime = get_uptime()

    print()
    print("=" * 45)
    print("             LINUX SYSTEM INFO")
    print("=" * 45)

    print("\n[ SYSTEM ]")
    print(f"OS:           {os_info['OS']}")
    print(f"Release:      {os_info['Release']}")
    print(f"Architecture: {os_info['Architecture']}")
    print(f"Hostname:     {os_info['Hostname']}")

    print("\n[ CPU ]")
    print(f"CPU cores:    {cpu_info['CPU cores']}")

    print("\n[ MEMORY ]")
    print(f"Total:        {memory['Total'] / 1024:.0f} MB")
    print(f"Used:         {memory['Used'] / 1024:.0f} MB")
    print(f"Available:    {memory['Available'] / 1024:.0f} MB")

    print("\n[ DISK ]")
    print(f"Total:        {disk['Total'] / (1024 ** 3):.1f} GB")
    print(f"Used:         {disk['Used'] / (1024 ** 3):.1f} GB")
    print(f"Free:         {disk['Free'] / (1024 ** 3):.1f} GB")

    print("\n[ UPTIME ]")
    print(f"Uptime:       {uptime}")

    print("\n" + "=" * 45)


if __name__ == "__main__":
    main()
