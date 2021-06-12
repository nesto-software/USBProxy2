#!/bin/bash

git clone https://github.com/usb-tools/ViewSB /tmp/viewsb
cd /tmp/viewsb && git checkout 3e9e10fab601cd3ddeb1dd70dace759009028eab && pip install --user -r requirements.txt && pip install --user .

git clone https://github.com/greatscottgadgets/luna.git /tmp/luna
cd /tmp/luna && git checkout 6f885cb0476f5387501ddfa7e5987a9d4f3b5c9a && poetry config virtualenvs.create false && poetry install
cd /tmp/luna && git checkout -b nesto && git remote add twam https://github.com/twam/luna/ && git fetch twam && GIT_MERGE_AUTOEDIT=no git merge twam/bugfix/116 nesto
# installed to: /home/mloeper/.cache/pypoetry/virtualenvs

pip install --user PySide2 nmigen

cd /home/mloeper/.cache/pypoetry/virtualenvs/luna-VJwzNawV-py3.9 && source ./bin/activate