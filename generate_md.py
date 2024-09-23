"""
This script generates a Markdown report from a CSV file containing data on banned maps.
It uses ydata-profiling to create a profile report and converts it to Markdown format.
"""

import os
import tempfile
import shutil
import requests
from bs4 import BeautifulSoup
import pandas as pd
from ydata_profiling import ProfileReport
from markdownify import markdownify

# Load your data
DATA_PATH = "data/rdu-weather-history"
df = pd.read_csv(DATA_PATH)

# Generate a profile report
profile = ProfileReport(df, title="Descriptive Statistics Report", explorative=True)

# Create a temporary directory for the HTML report and images
with tempfile.TemporaryDirectory() as temp_dir:
    temp_html_path = os.path.join(temp_dir, "report.html")

    # Save the HTML report
    profile.to_file(temp_html_path)

    # Parse the HTML and extract images
    with open(temp_html_path, "r", encoding="utf-8") as html_file:
        soup = BeautifulSoup(html_file, "html.parser")

    # Save images and update image paths
    image_paths = []
    for img_tag in soup.find_all("img"):
        img_src = img_tag.get("src")
        if img_src:
            # Create a new path for the image
            img_name = os.path.basename(img_src)
            img_dst_path = os.path.join(temp_dir, img_name)

            # Save the image
            try:
                response = requests.get(img_src, stream=True, timeout=10)
                response.raise_for_status()  # Ensure we notice bad responses
                with open(img_dst_path, "wb") as out_file:
                    shutil.copyfileobj(response.raw, out_file)
            except requests.RequestException as e:
                print(f"Failed to download image {img_src}: {e}")
                continue

            # Update image path in the HTML content
            img_tag["src"] = img_name
            image_paths.append(img_dst_path)

    # Convert HTML to Markdown with updated image paths
    H = str(soup)
    markdown_content = markdownify(H)

    # Write the Markdown content to a file
    with open("report.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    # Copy images to the current directory
    for img_path in image_paths:
        shutil.copy(img_path, ".")
