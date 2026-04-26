"""
capture.py — Camera capture utilities.

Responsible for opening the camera, reading frames, and releasing the device
cleanly when done. All other modules get their frames from here — nothing
else should talk to the camera directly.

Key concepts to understand before implementing:
- OpenCV represents a camera as a VideoCapture object. You open it with an
  index (0 = first USB camera) and read frames one at a time in a loop.
- Each frame is a NumPy array of shape (height, width, 3), where the 3
  channels are Blue, Green, Red (BGR) — note: NOT RGB. This trips people up
  when displaying colors.
- It's important to release the camera when you're done, or the device stays
  locked and other programs (or your next run) can't open it.
"""

import cv2


def open_camera(index: int = 0) -> cv2.VideoCapture:
    """Open the camera at the given device index and return the capture object.

    Try index=0 first. If that fails, try index=1 (some Pi setups expose
    a dummy device at 0 and the real camera at 1).
    """
    camera = cv2.VideoCapture(index)
    if not camera.isOpened():
        raise RuntimeError(f"camera at index {index} not found")
    else:
        return camera


def read_frame(cap: cv2.VideoCapture):
    """Read a single frame from an open VideoCapture. Returns a BGR NumPy array.

    cv2.VideoCapture.read() returns a tuple: (success_bool, frame).
    If success is False, the camera disconnected or the stream ended.
    """
    success, frame = cap.read()
    if success is not True:
        raise RuntimeError("camera read failed")
    else:
        return frame


def release_camera(cap: cv2.VideoCapture) -> None:
    """Release the camera device so other programs can use it."""
    cap.release()
