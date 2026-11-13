import tkinter as tk
import font_manager as fonts
import track_library as lib

def set_text(text_area, content):  # I made this function to update the text in a text box
    text_area.delete("1.0", tk.END)  # I clear the text box first
    text_area.insert(1.0, content)  # then I insert the new content

class CreateTrackList():
    def __init__(self, window):
        window.geometry("750x500")
        window.title("Create Track List")

        self.track_list = []  # I created an empty list to store the tracks the user adds

        # label to tell the user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        # small input box for the track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # button to add the track to the playlist
        add_track_btn = tk.Button(window, text="Add Track", command=self.add_track_clicked)
        add_track_btn.grid(row=0, column=2, padx=10, pady=10)

        # text area to display the playlist
        self.list_txt = tk.Text(window, width=48, height=10, wrap="none", bg="white", fg="black")
        self.list_txt.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # button to play the playlist
        play_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked)
        play_btn.grid(row=2, column=0, padx=10, pady=10)

        # button to reset and clear the playlist
        reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_btn.grid(row=2, column=1, padx=10, pady=10)

        # status label at the bottom, starts empty
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    def add_track_clicked(self):  # this runs when the user clicks Add Track
        key = self.input_txt.get().strip()  # I get the track number and remove any extra spaces
        if not key.isdigit():  # I check if the input is a number, if not I show an error
            self.status_lbl.configure(text="Please enter a valid track number!")
            return  # I stop the function here if the input is invalid
        name = lib.get_name(key)  # I check if that track exists in the library
        if name is not None:  # if the track was found
            self.track_list.append(name)  # I add the track name to my list
            track_display = "\n".join(self.track_list)  # I join all tracks with a new line
            set_text(self.list_txt, track_display)  # I display the updated playlist
            self.status_lbl.configure(text=f"{name} was added to the playlist!")
        else:  # if the track number wasnt found
            self.status_lbl.configure(text=f"Track {key} not found")

    def play_playlist_clicked(self):  # this runs when the user clicks Play Playlist
        if self.track_list:  # I check if there are any tracks in the playlist
            for track_name in self.track_list:  # I go through each track in the playlist
                for key in range(1, 6):  # I loop through track numbers to find the matching one
                    if lib.get_name(str(key).zfill(2)) == track_name:  # if the name matches
                        lib.increment_play_count(str(key).zfill(2))  # I increment the play count
            self.status_lbl.configure(text="Playlist has been played!")
        else:  # if the playlist is empty
            self.status_lbl.configure(text="Playlist is empty!")

    def reset_playlist_clicked(self):  # this runs when the user clicks Reset Playlist
        self.track_list = []  # I clear the track list
        set_text(self.list_txt, "")  # I clear the text area
        self.status_lbl.configure(text="Playlist has been reset!")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateTrackList(window)
    window.mainloop()