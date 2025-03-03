<h1>Image Colorization Application</h1>
The Image Colorization Application is a user-friendly tool that uses AI to transform grayscale and negative images into naturally colorized visuals. This project leverages deep learning models to bring old photographs, negatives, or monochrome images to life with vibrant and realistic colors.

________________________________________
<h3>Features</h3>

•🖼️ Grayscale Image Colorization: Automatically add realistic colors to grayscale images.

•	🔄 Negative Image Conversion: Detects and converts negative images to positive before applying colorization.

•	🎨 Enhanced Image Quality: Fine-tuned output with brightness, contrast, and saturation enhancements.

•	💻 Interactive Interface: Built with Streamlit for seamless uploads and real-time processing.

•	📥 Downloadable Output: Save the colorized image for further use or sharing.
________________________________________
<h3>How It Works</h3>

•	Upload: Select a grayscale or negative image in .jpg, .jpeg, or .png format.

•	Processing:

1. Grayscale images: Sent directly for colorization using the pre-trained model.

2.	Negative images: Converted to positive format and then colorized.

•	Enhancement: Brightness, contrast, and saturation are optimized for the final output.

•	Output: View and download the colorized image.

________________________________________
<h3>Getting Started</h3>

<h4>Clone this Repository</h4>

git clone https://github.com/yourusername/image-colorization-app.git

cd image-colorization-app

<h4>Install Dependencies</h4>

pip install -r requirements.txt

<h4>Download Model Files</h4>

This application uses the following model files:

•  colorization_release_v2.caffemodel

•  colorization_deploy_v2.prototxt

•  pts_in_hull.npy

Download these files and place them in the models folder.

<h4>Run the Application</h4>

streamlit run app.py

Visit http://localhost:8501 in your browser to use the application.

________________________________________
<h3>Applications</h3>

•  Restore old family photos or historical grayscale images.

•  Convert scanned negatives to vibrant, realistic pictures.

•  Enhance archival images for research or creative purposes.

<h3>Contributing</h3>

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

<h3>License</h3>

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.  