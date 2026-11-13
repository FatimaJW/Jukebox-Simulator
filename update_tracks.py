import tkinter as tk
import font_manager as fonts
import track_library as lib

def set_text(text_area, content):  # I made this function to update the text in a text box
    text_area.delete("1.0", tk.END)  # I clear the text box first
    text_area.insert(1.0, content)  # then I insert the new content

class UpdateTracks():
    def __init__(self, window):
        window.geometry("600x300")
        window.title("Update Tracks")

        # label and input for track number
        track_lbl = tk.Label(window, text="Enter Track Number")
        track_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.track_input = tk.Entry(window, width=3)
        self.track_input.grid(row=0, column=1, padx=10, pady=10)

        # label and input for new rating
        rating_lbl = tk.Label(window, text="Enter New Rating (1-5)")
        rating_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.rating_input = tk.Entry(window, width=3)
        self.rating_input.grid(row=1, column=1, padx=10, pady=10)

        # button to update the rating
        update_btn = tk.Button(window, text="Update Track", command=self.update_track_clicked)
        update_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # text box to show the result
        self.track_txt = tk.Text(window, width=40, height=4, wrap="none", bg="white", fg="black")
        self.track_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # status label at the bottom
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=2, sticky="W", padx=10, pady=10)

    def update_track_clicked(self):  # this runs when the user clicks Update Track
        key = self.track_input.get().strip()  # I get the track number and remove any spaces
        rating = self.rating_input.get().strip()  # I get the new rating
        if not key.isdigit():  # I check if the track number is a valid number
            self.status_lbl.configure(text="Please enter a valid track number!")
            return  # I stop here if invalid
        if not rating.isdigit() or not 1 <= int(rating) <= 5:  # I check if rating is between 1 and 5
            self.status_lbl.configure(text="Please enter a valid rating between 1 and 5!")
            return  # I stop here if invalid
        name = lib.get_name(key)  # I check if the track exists in the library
        if name is not None:  # if the track was found
            lib.set_rating(key, int(rating))  # I update the rating in the library
            play_count = lib.get_play_count(key)  # I get the play count
            track_details = f"{name}\nNew rating: {rating}\nPlay count: {play_count}"
            set_text(self.track_txt, track_details)  # I display the updated details
            self.status_lbl.configure(text="Track updated successfully!")
        else:  # if the track number wasnt found
            set_text(self.track_txt, f"Track {key} not found")
            self.status_lbl.configure(text="Track not found!")
if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTracks(window)
    window.mainloop()