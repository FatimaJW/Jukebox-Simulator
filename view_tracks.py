import tkinter as tk
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk
import track_library as lib
import font_manager as fonts


def set_text(text_area, content):  # I made this function to update the text in a text box
    text_area.delete("1.0", tk.END)  # I clear the text box first
    text_area.insert(1.0, content)  # then I insert the new content


class TrackViewer():
    def __init__(self, window):
        window.geometry("900x400")
        window.title("View Tracks")

        # List All Tracks button
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # label and input for track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # View Track button
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # I added a search box and button for searching tracks by name
        search_lbl = tk.Label(window, text="Search by Name")
        search_lbl.grid(row=2, column=0, padx=10, pady=10)

        self.search_txt = tk.Entry(window, width=15)
        self.search_txt.grid(row=2, column=1, padx=10, pady=10)

        search_btn = tk.Button(window, text="Search", command=self.search_tracks_clicked)
        search_btn.grid(row=2, column=2, padx=10, pady=10)

        # big scrollable text area for the track list
        self.list_txt = tkst.ScrolledText(window, width=48, height=10, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # smaller text box for individual track details
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # I added an image label to display a picture of the artist
        self.image_lbl = tk.Label(window)
        self.image_lbl.grid(row=1, column=4, padx=10, pady=10)

        # status label at the bottom
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked()

    def view_tracks_clicked(self):  # this runs when the user clicks View Track
        key = self.input_txt.get().strip()  # I get the track number the user typed
        if not key.isdigit():  # I check if the input is a valid number
            self.status_lbl.configure(text="Please enter a valid track number!")
            return
        name = lib.get_name(key)  # I look up the track in the library
        if name is not None:  # if the track was found
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
            self.show_image(key)  # I call my image function to show the artist picture
        else:
            set_text(self.track_txt, f"Track {key} not found")
            self.image_lbl.configure(image="")
        self.status_lbl.configure(text="View Track button was clicked!")

    def show_image(self, key):  # I added this method to display the artist image
        try:
            image = Image.open(f"{key}.jpg")  # I try to open the image file
            image = image.resize((150, 150))  # I resize it to fit the window
            photo = ImageTk.PhotoImage(image)  # I convert it to a format tkinter can display
            self.image_lbl.configure(image=photo)  # I display the image
            self.image_lbl.image = photo  # I keep a reference so it doesn't disappear
        except FileNotFoundError:  # if no image is found I just skip it
            self.image_lbl.configure(image="")

    def list_tracks_clicked(self):  # this runs when the user clicks List All Tracks
        track_list = lib.list_all()  # I get all the tracks from the library
        set_text(self.list_txt, track_list)  # I display them in the text area
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def search_tracks_clicked(self):  # I added this method to search tracks by name
        search_term = self.search_txt.get().strip().lower()  # I get the search term and make it lowercase
        if not search_term:  # if the search box is empty I show an error
            self.status_lbl.configure(text="Please enter a search term!")
            return
        results = ""
        for key in ["01", "02", "03", "04", "05"]:  # I loop through all tracks
            name = lib.get_name(key)
            if name and search_term in name.lower():  # I check if the search term matches
                artist = lib.get_artist(key)
                rating = lib.get_rating(key)
                results += f"{key} {name} - {artist} {'*' * rating}\n"
        if results:
            set_text(self.list_txt, results)
            self.status_lbl.configure(text=f"Search results for '{search_term}'")
        else:
            set_text(self.list_txt, "No tracks found!")
            self.status_lbl.configure(text="No matching tracks found!")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    TrackViewer(window)
    window.mainloop()
