"""
Script to get the total upload and download usage along with the speed
https://www.thepythoncode.com/article/make-a-network-usage-monitor-in-python
"""

import time
import psutil

from network_mon.utils import get_size

UPDATE_DELAY = 1  # in seconds


def network_usage_total() -> None:
    """Enter a loop that gets the same stats but after a delay so we can calculate the download and upload speed"""
    # get the network I/O stats from psutil
    io = psutil.net_io_counters(pernic=False)
    # extract the total bytes sent and received
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
    while True:
        # sleep for `UPDATE_DELAY` seconds
        time.sleep(UPDATE_DELAY)
        # get the stats again
        io_2 = psutil.net_io_counters()
        # new - old stats gets us the speed
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
        # print the total download/upload along with current speeds
        print(
            f"Upload: {get_size(io_2.bytes_sent)},   "
            f"Download: {get_size(io_2.bytes_recv)},   "
            f"Upload Speed: {get_size(us / UPDATE_DELAY)}/s,   "
            f"Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ",
            end="\r",
        )
        # update the bytes_sent and bytes_recv for next iteration
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv


if __name__ == "__main__":
    network_usage_total()
