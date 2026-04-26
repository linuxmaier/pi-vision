"""
display.py — Visualization helpers.

These functions draw information onto frames so you can see what the
program is "thinking" — bounding boxes around detected objects, the
boundary line, entry/exit labels, etc.

Visualization is essential for debugging vision code. If your motion
detector isn't working right, drawing the contours and masks on screen
is usually the fastest way to understand why.

Key concept: OpenCV drawing functions (cv2.rectangle, cv2.line, cv2.putText)
modify the frame array in place. They don't return a new image — they draw
directly onto the one you pass in. Keep that in mind so you don't
accidentally draw on a frame you wanted to keep clean.
"""

import cv2


def draw_boundary_line(frame, x: int) -> None:
    """Draw a vertical boundary line at the given x coordinate."""
    # TODO: use cv2.line to draw a vertical line from top to bottom of the frame.
    raise NotImplementedError


def draw_contour_box(frame, contour) -> None:
    """Draw a bounding rectangle around a contour."""
    # TODO: use cv2.boundingRect to get the box coords, then cv2.rectangle to draw it.
    raise NotImplementedError


def draw_label(frame, text: str, position: tuple) -> None:
    """Draw a text label at the given (x, y) position."""
    # TODO: use cv2.putText with a readable font and color.
    raise NotImplementedError


def show_frame(window_name: str, frame) -> bool:
    """Display a frame in a named window. Returns False if the user pressed 'q'."""
    # TODO: use cv2.imshow, then cv2.waitKey(1) and check for the 'q' key.
    raise NotImplementedError
