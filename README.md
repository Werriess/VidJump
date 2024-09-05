# VidJump

**VidJump** is a Tkinter-based application that allows users to search for specific words or phrases in YouTube video transcripts and jump directly to the relevant timestamps. Using the `youtube_transcript_api`, the app retrieves transcript data from YouTube videos and provides clickable links to the exact moments where the searched term appears.

## Features

- **Search by Keyword**: Enter a keyword or phrase to search for within a YouTube video's transcript.
- **Clickable Timestamps**: Get direct links to the timestamps in the video where the keyword appears.
- **User-Friendly Interface**: Simple and clean interface built with Tkinter.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Werriess/VidJump.git

2. **Clone to repository:**

   ```bash
   cd VidJump

3. **Install required dependencies:**

   ```bash
   pip install youtube-transcript-api tkhtmlview

## Usage

1. **Run application:**

   ```bash
      python main.py

2. **Enter a YouTube video URL:**
   - Paste the URL of the YouTube video into the "Paste in your YouTube link?" field.

3. **Enter a search term:**
   - Type the word or phrase you want to search for in the "What word are you searching for?" field.

4. **Click "Fetch":**
   - Click the "Fetch" button to retrieve the timestamps and see the results displayed below.

