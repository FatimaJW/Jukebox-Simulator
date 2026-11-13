# Jukebox Simulator

A jukebox simulator built in Python as part of my first-year Computing BSc at the University of Greenwich.


## Features
- View a list of tracks
-  Play tracks
- Create and update a track list


## Files
- `track_player.py`: The main window, with buttons to view tracks, create a track list and update tracks.
- `track_library.py`: Stores the five tracks in the library and has functions to list them all and look up a track's name, artist and rating by track number.
- `view_tracks.py`: A window that lists all the tracks.
- `create_track_list.py`: A window where you enter track numbers to build a playlist, play it, or reset it.
- `update_tracks.py`: A window where you enter a track number and a new rating (1-5) to update that track.
- `library_item.py`: the `LibraryItem` class, which holds a track's name, artist, star rating and play count.
- `font_manager.py`: Sets the fonts used across the app's windows.
- `test_library_item.py`: Pytest tests checking that `LibraryItem` stores the name, artist and rating correctly, starts with a play count of 0, and increments it.


## How to run

1. Install Python 3 from [python.org](https://www.python.org/downloads/)
2. Download or clone this repository
3. Open a terminal in the project folder
4. Run: `python3 track_player.py`


## How to run the tests

1. Install pytest: `pip3 install pytest`
2. In the project folder, run: `pytest`



## What I learned

- Building a GUI with Tkinter (windows, buttons, labels, text boxes)
- Using classes and objects to represent data
- Splitting a program across several files
- Writing simple automated tests with pytest



## Notes

- Album artwork isn't included in this repository for copyright reasons, so cover images may not display.
- This project was created for a university module and is shared here as a portfolio piece.
