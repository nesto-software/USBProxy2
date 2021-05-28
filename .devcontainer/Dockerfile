# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.177.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT} 

# install viewsb
RUN git clone https://github.com/usb-tools/ViewSB /tmp/viewsb
RUN cd /tmp/viewsb && git checkout 3e9e10fab601cd3ddeb1dd70dace759009028eab && pip install -r requirements.txt && pip install .

# install poetry
RUN pip3 install poetry 

# install luna (viewsb backend)
RUN git clone https://github.com/greatscottgadgets/luna.git /tmp/luna
RUN cd /tmp/luna && git checkout 6f885cb0476f5387501ddfa7e5987a9d4f3b5c9a && poetry config virtualenvs.create false && poetry install

# install facedancer (viewsb backend)
RUN git clone https://github.com/usb-tools/Facedancer.git /tmp/facedancer
RUN cd /tmp/facedancer && git checkout 28d3a900179e9dd280e007026a68fbdf97e4e35a && pip install .

# install PySide2 (viewsb frontend)
RUN pip install PySide2

# install some utilities for the user
RUN apt update && apt install -y usbutils

# install the FPGA toolchain

# prjtrellis:
# prerequisites:
RUN apt install -y build-essential cmake libboost-python-dev libboost-all-dev openocd

# download and prepare:
RUN git clone --recursive https://github.com/YosysHQ/prjtrellis /tmp/prjtrellis
RUN cd /tmp/prjtrellis && git checkout f93243b000c52b755c70829768d2ae6bcf7bb91a

# build and install:
RUN cd /tmp/prjtrellis/libtrellis \
    && cmake -DCMAKE_INSTALL_PREFIX=/usr . \
    && make -j$(nproc) \
    && make install

# YosysHQ/yosys:
# prerequisites:
RUN apt-get install -y build-essential clang bison flex \
	libreadline-dev gawk tcl-dev libffi-dev git \
	graphviz xdot pkg-config python3 libboost-system-dev \
	libboost-python-dev libboost-filesystem-dev zlib1g-dev 

# download and prepare:
RUN git clone https://github.com/YosysHQ/yosys.git /tmp/yosys
RUN cd /tmp/yosys && git checkout 2d10caabbc083cdb615ee2035916505758e4944f

# build and install:
RUN cd /tmp/yosys && make -j$(nproc) && make install

# YosysHQ/nextpnr:
# prerequisites:
RUN apt install -y libeigen3-dev libboost-all-dev python3-dev cmake 

# download and prepare
RUN git clone https://github.com/YosysHQ/nextpnr.git /tmp/nextpnr
RUN cd /tmp/nextpnr && git checkout e2b838a10a3eac7572d8702fb5353588aa80ec0c

# build and install:
RUN cd /tmp/nextpnr && cmake . -DARCH=ecp5 -DTRELLIS_INSTALL_PREFIX=/usr \
    && make -j$(nproc) \
    && make install

# nmigen:
# prerequisites
RUN apt-get install -y python3-pip gtkwave

# install
RUN pip3 install --upgrade nmigen


# install apollo-fpga package 
RUN pip install apollo-fpga

# install user shell config
RUN echo "#!/bin/sh\npython3 -m viewsb.commands.viewsb \$@" > /home/vscode/viewsb.sh && chmod +x /home/vscode/viewsb.sh
RUN echo 'alias viewsb="sudo /home/vscode/viewsb.sh"' >> /home/vscode/.bashrc

# patch luna code
RUN git config --global user.name "Nesto" && git config --global user.email "nesto@example.com"
RUN cd /tmp/luna && git checkout -b nesto && git remote add twam https://github.com/twam/luna/ && git fetch twam && GIT_MERGE_AUTOEDIT=no git merge twam/bugfix/116 nesto