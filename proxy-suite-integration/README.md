# Integration

This folder contains a python package that integrates LUNA into the ProxySuite.   
We read data from LUNA's USB analyzer and forward it onto the ZMQ layer.   
We add some meta information using msgpack.

The ideas are take from ViewSB's LUNA backend.

## Procedure

1. build and upload analyzer applet: https://github.com/greatscottgadgets/luna/blob/main/luna/gateware/applets/analyzer.py#L175
2. connect to the analyzer: https://github.com/greatscottgadgets/luna/blob/main/luna/gateware/applets/analyzer.py#L195
3. read packet: https://github.com/greatscottgadgets/luna/blob/main/luna/gateware/applets/analyzer.py#L212