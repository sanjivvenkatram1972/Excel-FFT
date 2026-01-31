# Free Throw Analyzer

A Python script for analyzing basketball free throw videos. Automatically reads video files from a configured directory with built-in validation and helpful error messages.

## Features

- 🎯 **Easy Configuration**: Simple config section at the top of the file
- 📂 **Automatic Video Discovery**: Lists available videos if file not found
- ✅ **File Validation**: Checks directory and file existence before processing
- 🌍 **Cross-Platform**: Works on Windows, Mac, and Linux
- 💡 **Helpful Error Messages**: Clear guidance when something goes wrong

## Quick Start

### 1. Place your video file

Put your free throw video in `C:/Python` (or any directory of your choice).

### 2. Update configuration

Edit the `VIDEO_CONFIG` section at the top of `free_throw_analyzer.py`:

```python
VIDEO_CONFIG = {
    'VIDEO_DIR': 'C:/Python',              # Your video directory
    'VIDEO_FILENAME': 'my_freethrow.mp4',  # Your video filename
    'RELEASE_FRAME': None                  # Auto-detect or specify frame number
}
```

### 3. Run the script

```bash
python free_throw_analyzer.py
```

## Supported Video Formats

- `.mp4`, `.MP4`
- `.mov`, `.MOV`
- `.avi`, `.AVI`
- `.mkv`, `.MKV`

## Configuration Options

### VIDEO_DIR
The directory containing your video files. Examples:
- Windows: `C:/Python` or `C:\\Users\\YourName\\Videos`
- Mac/Linux: `/home/user/videos` or `~/Videos`

### VIDEO_FILENAME
The name of your video file including extension. Example: `my_freethrow.mp4`

### RELEASE_FRAME
- `None`: Auto-detect release frame (default)
- Integer: Specify exact frame number (e.g., `42`)

## Error Messages

### Directory Not Found
```
❌ Error: Directory does not exist
   Directory: C:/Python

💡 Please create the directory or update VIDEO_CONFIG['VIDEO_DIR']
```

**Solution**: Create the directory or update `VIDEO_DIR` in the config.

### Video File Not Found
```
❌ Error: Video file not found
   Looking for: my_freethrow.mp4
   In directory: C:/Python

📹 Available video files in C:/Python:
   - shot1.mp4
   - shot2.mov
   - practice.avi

💡 Update VIDEO_CONFIG['VIDEO_FILENAME'] to one of the above
```

**Solution**: Either:
1. Rename your video to match `VIDEO_FILENAME`, or
2. Update `VIDEO_FILENAME` to match one of the available files

## Example Usage

```python
# Example 1: Default usage (auto-detect release frame)
VIDEO_CONFIG = {
    'VIDEO_DIR': 'C:/Python',
    'VIDEO_FILENAME': 'my_freethrow.mp4',
    'RELEASE_FRAME': None
}

# Example 2: Specify release frame manually
VIDEO_CONFIG = {
    'VIDEO_DIR': '/home/user/basketball_videos',
    'VIDEO_FILENAME': 'practice_shot_1.mov',
    'RELEASE_FRAME': 42  # Frame where ball is released
}

# Example 3: Using a different directory
VIDEO_CONFIG = {
    'VIDEO_DIR': '~/Documents/Sports/Basketball',
    'VIDEO_FILENAME': 'freethrow_analysis.mp4',
    'RELEASE_FRAME': None
}
```

## Technical Details

### Cross-Platform Path Handling

The script uses Python's `pathlib` module for cross-platform compatibility:

```python
from pathlib import Path
import os

# Works on all platforms
video_dir = Path(VIDEO_CONFIG['VIDEO_DIR'])
video_path = os.path.join(VIDEO_CONFIG['VIDEO_DIR'], VIDEO_CONFIG['VIDEO_FILENAME'])
```

### Helper Functions

#### `list_available_videos(directory)`
Lists all video files in the specified directory.

#### `validate_video_path(video_path)`
Validates that the video file exists and provides helpful error messages if not.

## Development

### Running Tests

The script includes comprehensive validation logic. To test manually:

```python
from free_throw_analyzer import list_available_videos, validate_video_path

# List videos in a directory
videos = list_available_videos('C:/Python')

# Validate a specific video path
is_valid = validate_video_path('C:/Python/my_video.mp4')
```

## Requirements

- Python 3.6+
- Standard library only (no external dependencies for basic functionality)

## License

This project is part of the Excel-FFT repository.
