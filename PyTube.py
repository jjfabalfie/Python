from pytube import YouTube

def download_video_with_subtitles(video_url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()
        # Display video details
        print("Downloading: {}".format(yt.title))
        print("Resolution: {}".format(video_stream.resolution))
        print("File Size: {:.2f} MB".format(video_stream.filesize / (1024 * 1024)))
        # Download the video to the specified output path
        video_stream.download(output_path)
        print("Download complete!")

    except Exception as e:
        print("Error: {}".format(str(e)))

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter YouTube video URL: ")
    download_video_with_subtitles(video_url)
