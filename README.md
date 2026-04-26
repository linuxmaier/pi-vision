# Pi Vision

A Raspberry Pi 5 machine vision learning project built by a parent and child.

The goal is to explore computer vision hands-on, starting simple and growing toward more complex tasks like tracking insects. The project is intentionally structured as a learning experience — code logic is worked through collaboratively rather than generated automatically.

## Hardware

- Raspberry Pi 5
- USB camera

## Milestones

1. Verify camera is accessible from Python on the Pi
2. Capture and display a live video frame
3. Detect motion using frame differencing
4. Detect entry/exit direction across a defined boundary line
5. *(Future)* Track small moving objects (e.g. ants)

## Setup

### 1. Flash the Pi

Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and flash **Raspberry Pi OS (64-bit)** to your SD card. Enable SSH and set your hostname/credentials during the imaging step.

### 2. Connect

```
ssh pi@<your-pi-hostname>.local
```

### 3. Identify the camera

```
lsusb
v4l2-ctl --list-devices
```

### 4. Set up Python environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Project Structure

```
pi-vision/
├── AGENTS.md           ← AI agent instructions (primary)
├── CLAUDE.md           ← symlink → AGENTS.md
├── README.md
├── requirements.txt
├── src/
│   ├── capture.py      ← camera capture utilities
│   ├── motion.py       ← motion detection logic
│   └── display.py      ← visualization helpers
└── tests/
```

## Key Concepts

See the docstrings in each `src/` module for explanations of the vision concepts used at each step. The learning path flows: **capture → diff → threshold → contours → boundary logic**.
