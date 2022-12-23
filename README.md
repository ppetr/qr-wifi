Create a PDF leaflet with WiFi QR code setup
============================================

This tool creates a PDF leaflet that contains a WiFi SSID, password and a QR
code that allows this information to be quickly scanned into a mobile phone.
Optionally also adds a custom message.

Useful if you want to share your WiFi with visitors, but your password is
something like 30 characters long.

Example
-------

Running

python qr-wifi.py --ssid Home --password sweethome \
           --output sample.pdf --message='No evil hacking!'

           produces:

![Example output](../../blob/docs/example.png?raw=true)

    Requirements
    ------------

    - Python version 2.7 or higher (for [argparse](https://docs.python.org/3/library/argparse.html)).
    - [Reportlab](https://pypi.python.org/pypi/reportlab).
    On Debian-based systems it's often available as a package and can be installed with

    sudo apt install python-reportlab
