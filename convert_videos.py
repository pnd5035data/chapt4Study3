import os
from moviepy import VideoFileClip

def convert_mov_to_mp4(input_folder, output_folder=None):
    """
    Convert all .mov files in input_folder to .mp4 format
    """
    if output_folder is None:
        output_folder = input_folder
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get all .mov files
    mov_files = [f for f in os.listdir(input_folder) if f.endswith('.mov')]
    
    print(f"Found {len(mov_files)} .mov files to convert")
    
    for i, mov_file in enumerate(mov_files, 1):
        input_path = os.path.join(input_folder, mov_file)
        mp4_file = mov_file.replace('.mov', '.mp4')
        output_path = os.path.join(output_folder, mp4_file)
        
        print(f"[{i}/{len(mov_files)}] Converting {mov_file} to {mp4_file}...")
        
        try:
            # Load the video
            clip = VideoFileClip(input_path)
            
            # Write to mp4
            clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
            
            # Close the clip to free memory
            clip.close()
            
            print(f"  [OK] Successfully converted {mov_file}")
            
        except Exception as e:
            print(f"  [ERROR] Error converting {mov_file}: {str(e)}")
    
    print(f"\nConversion complete! Converted {len(mov_files)} files.")

if __name__ == "__main__":
    videos_folder = "videos"
    output_folder = "videosMP4"
    convert_mov_to_mp4(videos_folder, output_folder)
