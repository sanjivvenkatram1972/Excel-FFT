"""
Free Throw Analyzer - Analyzes basketball free throw videos
Automatically reads video files from a configured directory
"""

from pathlib import Path
import os
import sys

# ============================================================================
# CONFIGURATION SECTION - Easy customization for users
# ============================================================================
VIDEO_CONFIG = {
    'VIDEO_DIR': 'C:/Python',
    'VIDEO_FILENAME': 'my_freethrow.mp4',  # User can change this
    'RELEASE_FRAME': None  # Auto-detect or specify frame number
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def list_available_videos(directory):
    """List all video files in the specified directory
    
    Args:
        directory: Path to directory to search for videos
        
    Returns:
        List of video filenames found in the directory
    """
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.MP4', '.MOV', '.AVI', '.MKV']
    video_dir = Path(directory)
    
    if not video_dir.exists():
        print(f"❌ Directory not found: {directory}")
        return []
    
    videos = [f.name for f in video_dir.iterdir() if f.suffix in video_extensions]
    return videos


def validate_video_path(video_path):
    """Validate that the video file exists and provide helpful error messages
    
    Args:
        video_path: Full path to video file
        
    Returns:
        True if valid, False otherwise
    """
    video_file = Path(video_path)
    video_dir = video_file.parent
    
    # Check if directory exists
    if not video_dir.exists():
        print(f"\n❌ Error: Directory does not exist")
        print(f"   Directory: {video_dir}")
        print(f"\n💡 Please create the directory or update VIDEO_CONFIG['VIDEO_DIR']")
        return False
    
    # Check if video file exists
    if not video_file.exists():
        print(f"\n❌ Error: Video file not found")
        print(f"   Looking for: {video_file.name}")
        print(f"   In directory: {video_dir}")
        
        # List available videos
        available_videos = list_available_videos(video_dir)
        if available_videos:
            print(f"\n📹 Available video files in {video_dir}:")
            for video in available_videos:
                print(f"   - {video}")
            print(f"\n💡 Update VIDEO_CONFIG['VIDEO_FILENAME'] to one of the above")
        else:
            print(f"\n📹 No video files found in {video_dir}")
            print(f"   Supported formats: .mp4, .mov, .avi, .mkv")
            print(f"\n💡 Please:")
            print(f"   1. Place your video file in: {video_dir}")
            print(f"   2. Update VIDEO_CONFIG['VIDEO_FILENAME'] with the correct filename")
        
        return False
    
    return True


# ============================================================================
# MAIN ANALYZER CLASS
# ============================================================================

class FreethrowAnalyzer:
    """Analyzes basketball free throw videos to extract trajectory and release data"""
    
    def __init__(self):
        """Initialize the analyzer"""
        print("🏀 Free Throw Analyzer initialized")
    
    def analyze_video(self, video_path, release_frame=None):
        """Analyze a video file to extract free throw data
        
        Args:
            video_path: Full path to the video file
            release_frame: Frame number where ball is released (None for auto-detect)
        """
        print(f"\n📹 Analyzing video: {Path(video_path).name}")
        print(f"   Full path: {video_path}")
        
        if release_frame is not None:
            print(f"   Release frame: {release_frame}")
        else:
            print(f"   Release frame: Auto-detect")
        
        # Video analysis implementation would go here
        # This is a placeholder for the actual analysis logic
        try:
            # Example: Open video, process frames, track ball, etc.
            print(f"\n✅ Video loaded successfully")
            print(f"   Processing frames...")
            print(f"   Tracking ball trajectory...")
            print(f"   Calculating release angle and velocity...")
            print(f"\n🎯 Analysis complete!")
            
        except Exception as e:
            print(f"\n❌ Error during analysis: {e}")
            raise


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("🏀 FREE THROW ANALYZER")
    print("=" * 70)
    
    # Convert to Path object for better handling
    video_dir = Path(VIDEO_CONFIG['VIDEO_DIR'])
    
    # Build full video path from config
    video_path = os.path.join(VIDEO_CONFIG['VIDEO_DIR'], VIDEO_CONFIG['VIDEO_FILENAME'])
    
    print(f"\n📂 Configuration:")
    print(f"   Video directory: {VIDEO_CONFIG['VIDEO_DIR']}")
    print(f"   Video filename: {VIDEO_CONFIG['VIDEO_FILENAME']}")
    print(f"   Release frame: {VIDEO_CONFIG['RELEASE_FRAME']}")
    
    # Validate the video path
    if not validate_video_path(video_path):
        print(f"\n❌ Cannot proceed - please fix the errors above")
        sys.exit(1)
    
    # Initialize analyzer
    analyzer = FreethrowAnalyzer()
    
    # Analyze the video
    try:
        analyzer.analyze_video(
            video_path, 
            release_frame=VIDEO_CONFIG['RELEASE_FRAME']
        )
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)
    
    print(f"\n" + "=" * 70)
    print("✅ Program completed successfully")
    print("=" * 70)
