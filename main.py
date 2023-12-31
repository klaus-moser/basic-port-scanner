#!/usr/bin/env python3

# Filename: main.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Basic port scanner. """


import sys
import time
import os
import socket
import logging

from datetime import datetime
from tqdm import tqdm

__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = time.ctime(os.path.getmtime(__file__))


def print_logo() -> None:
    """
    Print logo from "logo.txt" file.

    :return:
    """

    try:
        with open(file="logo.txt") as l:
            logo = l.readlines()
        for line in logo:
            print(line, end="")
        print("\nVersion:\t" + __version__ + "\nAuthor(s):\t" + __author__ + "\nLast Mod.: " + __date__ + "\n")

    except FileNotFoundError as e:
        print("(logo?)")


def port_scanner(target: str) -> None:
    """
    Base function of the port scanner.

    :return:
    """

    print_logo()  # Add a pretty banner
    print("-" * 50)
    print("Scanning target " + target)
    print("Time started: " + str(datetime.now()))
    print("-" * 50)

    try:
        results = list()

        for port in tqdm(range(50, 85), "Scanning..."):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))  # returns error indicator - port=open throws a 0, otherwise 1

            if result == 0:
                results.append("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    except socket.error:
        print("Could not connect to server.")
        sys.exit()

    if results:
        print("\nResults: \n")
        for result in results:
            print(result)
    else:
        print("All ports are closed!\n\n")


if __name__ == '__main__':
    if len(sys.argv) == 2:  # Define our target
        ip = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
    else:
        print("Invalid amount of arguments.")
        print("Syntax: python3 scanner.py")
        sys.exit()

    port_scanner(target=ip)
