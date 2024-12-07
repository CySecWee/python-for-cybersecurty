import psutil
import time
from rich.console import Console
from rich.table import Table

UPDATE_DELAY = 1  # in seconds
console = Console()

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def monitor_network():
    """
    Monitor network stats and display dynamically using rich.
    """
    # Initial network stats
    io = psutil.net_io_counters(pernic=True)

    while True:
        time.sleep(UPDATE_DELAY)
        # Get updated network stats
        io_2 = psutil.net_io_counters(pernic=True)
        data = []

        # Calculate upload and download speeds
        for iface, iface_io in io.items():
            upload_speed = io_2[iface].bytes_sent - iface_io.bytes_sent
            download_speed = io_2[iface].bytes_recv - iface_io.bytes_recv
            data.append({
                "Interface": iface,
                "Download": get_size(io_2[iface].bytes_recv),
                "Upload": get_size(io_2[iface].bytes_sent),
                "Download Speed": f"{get_size(download_speed / UPDATE_DELAY)}/s",
                "Upload Speed": f"{get_size(upload_speed / UPDATE_DELAY)}/s",
            })

        # Update the previous stats
        io = io_2

        # Create a table for displaying network stats
        table = Table(title="Network Interface Monitor")

        table.add_column("Interface", justify="left", style="cyan", no_wrap=True)
        table.add_column("Download", justify="right", style="green")
        table.add_column("Upload", justify="right", style="green")
        table.add_column("Download Speed", justify="right", style="magenta")
        table.add_column("Upload Speed", justify="right", style="magenta")

        for entry in data:
            table.add_row(
                entry["Interface"],
                entry["Download"],
                entry["Upload"],
                entry["Download Speed"],
                entry["Upload Speed"],
            )

        # Clear the console and print the table
        console.clear()
        console.print(table)

if __name__ == "__main__":
    try:
        monitor_network()
    except KeyboardInterrupt:
        console.print("[bold red]Exiting...[/bold red]")
