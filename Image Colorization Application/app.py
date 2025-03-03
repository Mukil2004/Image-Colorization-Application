import streamlit as st
from PIL import Image
import numpy as np
import cv2
import io
import os

# Set up Streamlit app
st.title("Image Converter: Natural Colorization")
st.write("Upload a grayscale or negative image to get realistic colorization.")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Model file paths
prototxt = "colorization_deploy_v2.prototxt"
model = "colorization_release_v2.caffemodel"
points = "pts_in_hull.npy"

# Check for required model files
if not os.path.exists(prototxt) or not os.path.exists(model) or not os.path.exists(points):
    st.error("Model files missing! Download them from:")
    st.markdown("- [colorization_deploy_v2.prototxt](https://github.com/richzhang/colorization/raw/master/models/colorization_deploy_v2.prototxt)")
    st.markdown("- [colorization_release_v2.caffemodel](http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel)")
    st.markdown("- [pts_in_hull.npy](https://github.com/richzhang/colorization/raw/master/resources/pts_in_hull.npy)")
    st.stop()

# Load the model
net = cv2.dnn.readNetFromCaffe(prototxt, model)
pts = np.load(points)
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

def preprocess_image(img_array):
    """Adjust gamma for better brightness/contrast."""
    gamma = 1.2
    look_up_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    adjusted = cv2.LUT(img_array, look_up_table)
    return adjusted

def colorize_grayscale(img_array):
    """Colorize a grayscale image."""
    normalized = img_array.astype("float32") / 255.0
    lab = cv2.cvtColor(normalized, cv2.COLOR_RGB2LAB)
    L = cv2.split(lab)[0]
    L -= 50

    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (img_array.shape[1], img_array.shape[0]))
    L = cv2.split(lab)[0]

    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2RGB)
    colorized = (255 * colorized).astype("uint8")
    return colorized

def detect_image_type(img_array):
    """Detect if the image is grayscale or negative."""
    if len(img_array.shape) == 2 or np.array_equal(img_array[:, :, 0], img_array[:, :, 1]):
        return "grayscale"
    elif np.all(img_array <= 255) and np.mean(img_array) < 128:  # Check for high-intensity inversion
        return "negative"
    else:
        return "color"

if uploaded_file:
    # Load and display the input
    input_image = Image.open(uploaded_file).convert("RGB")
    st.subheader("Uploaded Image")
    st.image(input_image, use_container_width=True)

    # Convert to numpy array
    img_array = np.array(input_image)

    # Detect grayscale or negative
    image_type = detect_image_type(img_array)
    if image_type == "grayscale":
        st.subheader("Detected Grayscale Image")
        img_array = preprocess_image(img_array)
        colorized = colorize_grayscale(img_array)
    elif image_type == "negative":
        st.subheader("Detected Negative Image")
        positive = 255 - img_array
        colorized = colorize_grayscale(preprocess_image(positive))
    else:
        st.error("Uploaded image is not grayscale or negative. Please upload a valid image.")
        st.stop()

    # Enhance the output image
    colorized = cv2.cvtColor(colorized, cv2.COLOR_RGB2HSV)
    colorized[:, :, 1] = cv2.add(colorized[:, :, 1], 15)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_HSV2RGB)

    # Display the result
    st.subheader("Natural Colorized Image")
    st.image(colorized, use_container_width=True)

    # Provide download link
    buf = io.BytesIO()
    Image.fromarray(colorized).save(buf, format="PNG")
    buf.seek(0)
    st.download_button(
        label="Download Colorized Image",
        data=buf.getvalue(),
        file_name="colorized.png",
        mime="image/png"
    )
