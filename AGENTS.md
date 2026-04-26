# AGENTS.md — Pi Vision Project

> **Primary source of truth.** `CLAUDE.md` is a symlink pointing here. Always edit `AGENTS.md` directly, never `CLAUDE.md`.

---

## Project Overview

This is a learning-focused Raspberry Pi 5 machine vision project. The hardware is a Raspberry Pi 5 with a USB camera. The goal is to explore computer vision concepts hands-on — starting with simple tasks (e.g. detecting whether people are entering or leaving a camera frame) and growing toward more complex ones (e.g. tracking insects to their origin point).

This project is being built by a parent and child together as a learning experience.

---

## Guiding Principles for AI Agents

### 1. Teach, Don't Just Do

The primary purpose of this project is education. When a coding task arises that involves meaningful logic, **explain the approach and the reasoning first**, then ask whether to proceed. Do not silently implement algorithms or vision pipelines — walk through:

- What the code is doing conceptually
- Why a particular approach is chosen over alternatives
- What the user will observe when it runs

### 2. What Agents May Do Without Prompting

- Create file stubs (empty modules, placeholder functions with docstrings)
- Set up project scaffolding (directory structure, `__init__.py`, config files)
- Manage `AGENTS.md` updates (see principle 5)
- Add or update `.gitignore`, `requirements.txt`, `README.md`
- Fix routine syntax errors or obvious typos when asked to debug
- Run shell commands to check system state (e.g. `lsusb`, `vcgencmd`, `pip list`)

### 3. What Agents Should Guide, Not Implement

- Any logic that detects, tracks, or classifies objects
- Frame-differencing, background subtraction, contour detection
- Any model inference or embedding logic
- Calibration routines or threshold-setting logic
- Any algorithm the learner should understand before using

For these, the agent should explain the concept, show a minimal pseudocode sketch or reference, and invite the user to attempt the implementation before offering help.

### 4. Explain the Platform

When commands or code choices are specific to Raspberry Pi, Linux on ARM, or the camera setup, explain the "why" — e.g. why `v4l2` is used, what `libcamera` does differently, why GPIO numbering matters. These platform-specific details are easy to cargo-cult without understanding.

### 5. Keep AGENTS.md Current

Whenever something non-obvious is learned about the platform, the camera, or the project's constraints, **add a note to AGENTS.md** in the relevant section below. This file acts as accumulated institutional knowledge for the project. Update it proactively — don't wait to be asked.

### 6. Commit Messages

When committing code that addresses a runtime bug, mention the bug at the top of the commit message. Follow conventional commit style where practical.

---

## Platform Notes

*This section grows as we learn. Agents should add to it.*

### Hardware

- **Board:** Raspberry Pi 5
- **Camera:** USB camera (model TBD — run `lsusb` to identify)
- **OS:** TBD — confirm with `uname -a` and `cat /etc/os-release` on first connection

### Camera Access

- USB cameras on Linux appear as `/dev/video0` (or `/dev/video1`, etc.). Use `v4l2-ctl --list-devices` to enumerate them.
- The Raspberry Pi 5 also supports the official camera module via `libcamera`, but for USB cameras the standard Video4Linux2 (v4l2) stack is used.
- OpenCV can open a USB camera with `cv2.VideoCapture(0)` — the integer corresponds to the `/dev/videoN` index.

### Python Environment

- Use a dedicated virtual environment (conda or venv) for this project. Never install into system Python.
- Core libraries: `opencv-python`, `numpy`, `pytest`. `picamera2` is only relevant for the Pi camera module, not USB cameras.
- Machine-specific environment details (env name, interpreter path) are recorded in `local_management/environment.md` — check there first.

### Laptop Development

- The code is fully portable. A Linux laptop with a USB or built-in webcam is a valid development environment — no Pi required.
- OpenCV's `VideoCapture` works identically on both platforms. The webcam on the development laptop appears at `/dev/video0` and returns 640×480 BGR frames.
- The only things that differ on the Pi: slower CPU, possibly a different `/dev/videoN` index, and headless display considerations if running over SSH.

### Useful Diagnostic Commands

```bash
lsusb                        # list USB devices (identify camera model)
v4l2-ctl --list-devices      # list video capture devices
v4l2-ctl -d /dev/video0 --all  # full capabilities of a device
uname -a                     # kernel / architecture
vcgencmd measure_temp        # Pi CPU temperature
```

---

## Project Milestones

1. **[Done]** Project setup and AGENTS.md scaffolding
2. **[Done]** Implement `capture.py` — verified working on laptop webcam (640×480 BGR frames)
3. Capture and display a live video frame (`display.py`)
4. Detect motion in the frame (frame differencing)
5. Detect entry/exit direction across a defined boundary line
6. (Future) Ant tracking — detect and follow small moving objects

---

## File Layout (planned)

```
pi-vision/
├── AGENTS.md           ← this file (primary)
├── CLAUDE.md           ← symlink → AGENTS.md
├── README.md
├── requirements.txt
├── src/
│   ├── capture.py      ← camera capture utilities
│   ├── motion.py       ← motion detection logic (learner implements)
│   └── display.py      ← optional visualization helpers
└── tests/
```
