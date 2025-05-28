import os
from glob import glob
def generate_video_grid_html(output_file, video_list):
    """
    Generates an HTML file displaying a grid of images with 2 images per row.
    
    Args:
        output_file (str): The path to save the HTML file.
        image_list (list): List of image file paths to be displayed.
    """
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Grid</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f0f0f0;
            padding: 20px;
        }
        .block {
            display: flex;
            flex-direction: column;
            width: 100%;
            margin-bottom: 60px;
            clear: both;
            
            display: flex;
            flex-direction: column;
            width: 100%;
            clear: both;
            margin-bottom: 40px;
            display: block;
            width: 100%;
            margin-bottom: 30px;
            display: flex;
            flex-direction: column;
            width: 100%;
            width: 100%; max-width: 80%;
            margin-bottom: 30px;
        }
        .block-title {
            text-align: center;
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);grid-auto-rows: 1fr; 
            gap: 10px;
            width: 75%;
            clear: both;
            margin-top: 20px;
        }
        .grid-container img {
            width: 100%; height: 100%; object-fit: contain; max-height: 200px;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }
        .grid-header {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            font-weight: bold;
            text-align: center;
            padding-bottom: 10px;
        }
        .grid-container video {
            width: 100%; height: 100%; object-fit: contain;  max-height: 300px;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>          
"""
    
    html_content += f'<div class="grid-container">'
    for video in video_list:
        html_content += f'            <video controls><source src="{video}" type="video/mp4"></video>\n'
        
    html_content += """</div>"""
    with open(output_file, "w") as file:
        file.write(html_content)
    
    print(f"HTML file generated: {output_file}")


music_dir = "everyone_unique_dance/CannotStopFeeling"
video_paths = sorted(glob(os.path.join(music_dir, '*.mp4')))
video_paths = [os.path.basename(video_path) for video_path in video_paths]
if 'demo.mp4' in video_paths:
    video_paths.remove('demo.mp4')

output_file = os.path.join(music_dir, 'index.html')
generate_video_grid_html(output_file,video_paths)
                         
