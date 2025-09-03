import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.title("🎥 Real-time Color Detection with Webcam")

# Sidebar for selecting color
color_option = st.sidebar.selectbox(
    "Choose a color to detect:",
    ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
)

# Define HSV color ranges
color_ranges = {
    "Red": ([161, 155, 84], [179, 255, 255]),
    "Green": ([40, 100, 100], [102, 255, 255]),
    "Blue": ([94, 80, 2], [126, 255, 255]),
    "Yellow": ([20, 100, 100], [30, 255, 255]),
    "Orange": ([10, 100, 20], [25, 255, 255]),
    "Purple": ([129, 50, 70], [158, 255, 255])
}


class ColorDetection(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Get selected color HSV range
        lower, upper = color_ranges[color_option]
        lower = np.array(lower)
        upper = np.array(upper)

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)

        return result


# Start webcam stream
webrtc_streamer(
    key="example",
    video_transformer_factory=ColorDetection,
    media_stream_constraints={"video": True, "audio": False},
)
