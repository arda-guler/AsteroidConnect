import os

image_dir = "data/itf2des_img"
text_dir = "data/itf2des_obs80"
output_file = "data.html"

html_content = """
<div id="data-container">
"""

for image_file in os.listdir(image_dir):
    if image_file.endswith(".jpg") or image_file.endswith(".png"):
        text_file = os.path.splitext(image_file)[0] + ".txt"
        if os.path.exists(os.path.join(text_dir, text_file)):
            html_content += f"""
            <div class="data-box">
                <img src="{image_dir}/{image_file}" alt="{image_file}">
                <iframe src="{text_dir}/{text_file}"></iframe>
            </div>
            """

html_content += """
</div>
"""

with open(output_file, "w") as f:
    f.write(html_content)

print(f"HTML content saved to {output_file}")
