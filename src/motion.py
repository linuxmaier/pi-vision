"""
motion.py — Motion detection and entry/exit logic.

This is the heart of the project. It will eventually answer the question:
"did something move, and was it moving INTO or OUT OF the frame?"

We'll build this up in stages:
  1. Frame differencing — compare two consecutive frames to find what changed.
  2. Thresholding — turn the difference into a black-and-white mask.
  3. Contour detection — find the blobs in the mask (those are moving objects).
  4. Boundary logic — decide whether a blob crossed a line, and in which direction.

None of this is implemented yet. Work through the concepts in AGENTS.md and
with your instructor before filling anything in here.
"""

import numpy as np


def compute_frame_diff(frame_a, frame_b):
    """Return a grayscale image showing pixels that changed between two frames.

    Key concepts:
    - Convert both frames to grayscale first (motion doesn't care about color).
    - Subtract one from the other with cv2.absdiff — this gives you the
      magnitude of change at each pixel.
    - The result is still a grayscale image, not yet a binary mask.
    """
    # TODO: implement frame differencing.
    raise NotImplementedError


def threshold_diff(diff_frame, threshold: int = 25):
    """Convert a grayscale diff image into a binary mask.

    Pixels brighter than `threshold` become white (255); everything else black.
    This separates "definitely moved" from "just sensor noise."

    Key concept: cv2.threshold with cv2.THRESH_BINARY is the tool here.
    """
    # TODO: implement thresholding.
    raise NotImplementedError


def find_motion_contours(binary_mask):
    """Find contours (outlines of blobs) in a binary mask.

    Returns a list of contours. Each contour is an array of (x, y) points
    tracing the edge of one moving region.

    Key concept: cv2.findContours — pay attention to the retrieval mode and
    approximation method arguments; they control how much detail you get.
    """
    # TODO: implement contour detection.
    raise NotImplementedError


def classify_crossing(contour, boundary_x: int, prev_cx: int):
    """Determine whether a contour crossed the boundary line.

    Arguments:
        contour    -- a single contour from find_motion_contours
        boundary_x -- the x-coordinate of the vertical boundary line
        prev_cx    -- the x-coordinate of this object's center in the previous frame

    Returns 'enter', 'exit', or None.

    Key concept: compute the centroid (center point) of the contour using
    cv2.moments, then compare its x position to the boundary and to where it
    was last frame.
    """
    # TODO: implement crossing logic.
    raise NotImplementedError
