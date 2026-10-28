#!/bin/bash
# Take a set of headless screenshots of a running SilverBullet (expected on 127.0.0.1:3111).
# usage: tools/run.sh <name>   -> writes shots/<name>-{light,dark}-{index,atlas,picker,mobile}.png
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/shots"
docker build --network host -q -t sb-shooter "$ROOT/tools" >/dev/null
docker run --rm --network host --ipc=host -v "$ROOT":/work sb-shooter \
  python -I /work/tools/shoot.py "/work/shots/$1"
