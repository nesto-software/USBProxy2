import usb
import errno

from luna.gateware.applets.analyzer     import BULK_ENDPOINT_ADDRESS, MAX_BULK_PACKET_SIZE
from datetime import datetime

def fetch_data_into_buffer(device, buffer):
    """ Attempts a single data read from the analyzer into our buffer. """

    try:
        data = device.read(BULK_ENDPOINT_ADDRESS, MAX_BULK_PACKET_SIZE)
        buffer.extend(data)
    except usb.core.USBError as e:
        if e.errno == errno.ETIMEDOUT:
            pass
        else:
            raise

def read_raw_packet(device, buffer):
    """ Reads a raw packet from our USB Analyzer. Blocks until a packet is complete.
    Returns: packet, timestamp, flags:
        packet    -- The raw packet data, as bytes.
        timestamp -- The timestamp at which the packet was taken, in microseconds.
        flags     -- Flags indicating connection status. Format TBD.
    """

    size = 0
    packet = None

    # Read until we get enough data to determine our packet's size...
    while not packet:
        while len(buffer) < 3:
            fetch_data_into_buffer(device, buffer)

        # Extract our size from our buffer.
        size = (buffer.pop(0) << 8) | buffer.pop(0)

        # ... and read until we have a packet.
        while len(buffer) < size:
            fetch_data_into_buffer(device, buffer)

        # Extract our raw packet...
        packet = buffer[0:size]
        del buffer[0:size]

    return packet, datetime.now(), None