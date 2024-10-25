import os
import re
import moviepy.editor as mp

# Input variables
folder_path = '4'  # Change this path to your desired folder
output_filename = '4.mp4'
speed_factor = 4.0  # 1.0 means normal speed, 2.0 is double speed, etc.

def get_mp4_files_sorted(folder):
    """Retrieve and sort MP4 files from the specified folder based on day and iteration."""
    def extract_sort_key(filename):
        # Use regex to extract day and iteration from the filename (e.g., inktober_4-1.mp4)
        match = re.search(r'inktober_(\d+)-(\d+)\.mp4', filename)
        if match:
            day = int(match.group(1))
            iteration = int(match.group(2))
            return (day, iteration)
        return (0, 0)  # Default for files not matching the pattern

    mp4_files = [f for f in os.listdir(folder) if f.endswith('.mp4')]
    mp4_files.sort(key=extract_sort_key)
    return [os.path.join(folder, f) for f in mp4_files]

def stitch_mp4s(mp4_files, output, speed):
    """Stitch MP4 files together and adjust speed."""
    clips = [mp.VideoFileClip(f).fx(mp.vfx.speedx, speed) for f in mp4_files]
    final_clip = mp.concatenate_videoclips(clips)
    final_clip.write_videofile(output, codec='libx264')

if __name__ == '__main__':
    mp4_files = get_mp4_files_sorted(folder_path)
    if mp4_files:
        stitch_mp4s(mp4_files, output_filename, speed_factor)
        print(f"Output saved as {output_filename}")
    else:
        print("No MP4 files found in the specified folder.")
