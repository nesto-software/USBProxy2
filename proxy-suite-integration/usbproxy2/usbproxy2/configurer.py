from luna.gateware.applets.analyzer       import USBAnalyzerApplet
from luna                                 import get_appropriate_platform

def build_and_configure(capture_speed):
        """ Builds the LUNA analyzer applet and configures the FPGA with it. """

        # Create the USBAnalyzer we want to work with.
        analyzer = USBAnalyzerApplet(usb_speed=capture_speed)

        # Build and upload the analyzer.
        # FIXME: use a temporary build directory
        platform = get_appropriate_platform()
        platform.build(analyzer, do_program=True)
