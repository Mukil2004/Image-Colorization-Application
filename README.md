Image Colorization Application
Overview
The Image Colorization Application is a user-friendly tool that uses AI to transform grayscale and negative images into naturally colorized visuals. This project leverages deep learning models to bring old photographs, negatives, or monochrome images to life with vibrant and realistic colors.

Features
🖼️ Grayscale Image Colorization: Automatically add realistic colors to grayscale images.
🔄 Negative Image Conversion: Detects and converts negative images to positive before applying colorization.
🎨 Enhanced Image Quality: Fine-tuned output with brightness, contrast, and saturation enhancements for visually appealing results.
💻 Interactive Interface: Built with Streamlit, offering seamless uploads and real-time processing.
📥 Downloadable Output: Save the colorized image for further use or sharing.
How It Works
Upload: Select a grayscale or negative image in .jpg, .jpeg, or .png format.
Processing:
Grayscale images: Sent directly for colorization using a pre-trained deep learning model.
Negative images: Converted to positive format and then colorized.
Enhancement: The processed image is enhanced for brightness, contrast, and saturation.
Output: View the colorized image in the app and download it as a .png file.
Technologies Used
Framework: Streamlit for building the web interface.
Deep Learning Model: Pre-trained Caffe model:
colorization_release_v2.caffemodel
colorization_deploy_v2.prototxt
pts_in_hull.npy (color distribution data)
Libraries:
OpenCV: Image processing and model integration.
NumPy: Image preprocessing.
Pillow: For image handling and file manipulation.
