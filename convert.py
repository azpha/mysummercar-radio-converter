import sys
import os
import subprocess
import shutil

def main():
    try:
        subprocess.run("ffmpeg -version", stdout=subprocess.PIPE)
    except FileNotFoundError as e:
        print("FFmpeg does not exist! Did you install it?")
    except subprocess.SubprocessError:
        print("An error occurred trying to run FFmpeg!")

    # get msc directory to drop radio files in
    msc_directory = input("Where is the MSC 'steamapps/common' directory? ")
    if not os.path.exists(os.path.join(msc_directory, 'Radio')):
        print("That directory doesn't exist!")
        sys.exit(1)
    
    # check for songs
    if not os.path.exists('./music'):
        print("No music directory found! Create one in this directory.")
        sys.exit(1)
    if len(os.listdir('./music')) == 0:
        print("No music found in directory! Add some files.")
        sys.exit(1)

    # start conversion
    files = os.listdir('./music')
    files_made = 0
    os.mkdir('./music/completed')
    for file in files:
        if ".mp3" in file:
            full_path = os.path.join('./music', file)
            ffmpeg_command = f'ffmpeg -i "{full_path}" -c:a libvorbis -q:a 4 ./music/completed/track{files_made + 1}.ogg'
            subprocess.run(ffmpeg_command)

            files_made += 1
        else:
            print(f"'.mp3' extension not in {file}, skipping")
    
    # complete, move to msc directory
    print("Conversion process complete!")
    if len(os.listdir('./music/completed')) == 0:
        print("No files converted! Did you have mp3 files in the directory?")
        sys.exit(1)
    
    # move to MSC directory
    for file in os.listdir('./music/completed'):
        path = os.path.join('./music/completed', file)
        shutil.move(path, os.path.join(msc_directory, "Radio", file))
    shutil.rmtree('./music/completed')


if __name__ == "__main__":
    main()