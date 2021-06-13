import time
import usb
from luna.gateware.applets.analyzer     import USB_VENDOR_ID, USB_PRODUCT_ID, USB_SPEED_HIGH, USB_SPEED_FULL, USB_SPEED_LOW
from usbproxy2.reader import read_raw_packet
from usbproxy2.configurer import build_and_configure
from viewsb.packet import USBPacket

print("Configuring the board with USB analyzer...")
build_and_configure(USB_SPEED_FULL)
print("The board is configured to act as a USB analyzer now. Waiting some time for the OS to recognize the device...")

time.sleep(10)

print("Connecting to device...")
device = usb.core.find(idVendor=USB_VENDOR_ID, idProduct=USB_PRODUCT_ID)

if device == None:
    print("Could not find analyzer. Make sure the board is plugged in and configured correctly.")
    exit(1)

print("Connected.")

buffer = bytearray()

# sophisticated logic see: https://github.com/usb-tools/ViewSB/blob/3e9e10fab601cd3ddeb1dd70dace759009028eab/viewsb/analyzer.py
# issue 1: must flash device each time analysis port is (re-)connected and board is powered on
# issue 2: must plugin in device after flashing device because otherwise overrun occurs
# issue 3: overrun during print job, see also: https://github.com/greatscottgadgets/luna/milestone/8
while True:
    print("Reading packet...")
    raw_packet, timestamp, _ = read_raw_packet(device, buffer)
    packet = USBPacket.from_raw_packet(raw_packet, timestamp=timestamp)
    if packet.summarize() != "SOF packet":
        print(packet)