# Jukebox Simulator

A jukebox simulator built in Python as part of my first-year Computing BSc at the University of Greenwich.


## Features
- View a list of tracks
- e.g. Play tracks
- e.g. Create and update a track list


## Files
- `track_player.py`: The main window, with buttons to view tracks, create a track list and update tracks.
- `track_library.py`: Stores the five tracks in the library and has functions to list them all and look up a track's name, artist and rating by track number.
- `view_tracks.py`: A window that lists all the tracks.
- `create_track_list.py`: A window where you enter track numbers to build a playlist, play it, or reset it.
- `update_tracks.py`: A window where you enter a track number and a new rating (1-5) to update that track.
- `library_item.py`: the `LibraryItem` class, which holds a track's name, artist, star rating and play count.
- `font_manager.py`: Sets the fonts used across the app's windows.
- `test_library_item.py`: Pytest tests checking that `LibraryItem` stores the name, artist and rating correctly, starts with a play count of 0, and increments it.
