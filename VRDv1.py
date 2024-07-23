import requests # import request module for the request to the API
import datetime # import datetime module for the current year
import tkinter as tk # import module for windows creation
import webbrowser # import module to hypertext link

def get_games_on_date(year, month, day): # function to request the date
    base_url = "https://api.rawg.io/api/games"
    date_range = f"{year}-{month:02d}-{day:02d},{year}-{month:02d}-{day:02d}"
    params = {
        "dates": date_range,
        "ordering": "-released",
        "key": "*********************************", # use your owen API KEY from RAWG.IO
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        games = data.get("results", [])
        return games
    else:
        print(f"Error fetching data for {year}: {response.status_code}")
        return []
    
def weblink1(): # Link whom open my website ;)
    
    webbrowser.open("https://rogeliovr.github.io/Roge.pro/")


def search_games():
    try:
        month = int(month_entry.get())
        day = int(day_entry.get())

        results_text.delete(1.0, tk.END) # Clean the text area box

        start_year = 1958
        current_year = datetime.datetime.now().year

        for year in range(start_year, current_year + 1):
            games = get_games_on_date(year, month, day)
            if games:
                results_text.insert(tk.END, f"Games released in {month:02d}/{day:02d}/{year}:\n")
                for game in games:
                    results_text.insert(tk.END, f"- {game['name']}\n")
            else:
                results_text.insert(tk.END, f"No video games found for {year}.\n")
    except ValueError:
        results_text.insert(tk.END, "Please insert month and day valid numbers")

def main():

    global month_entry, day_entry, results_text  # Globals
    # Tkinter windows
    root = tk.Tk()
    root.title("VRD - V 0.1")
    root.geometry("500x570")

    title_label = tk.Label(root, text="VRD", font=("Helvetica", 24, "bold"))
    subtitle_label = tk.Label(root, text="Videogames Release Date", font=("Helvetica", 16))
    credits_label = tk.Label(root, text="https://rogeliovr.github.io/Roge.pro/", font=("Helvetica", 12), fg="blue", cursor="hand2")
    credits_label.bind("<Button-1>", lambda e: weblink1())

    instructions1_label = tk.Label(root, text="Instructions: Insert month and day", font=("Helvetica", 12))

    month_label = tk.Label(root, text="Month", font=("Helvetica", 12))
    month_entry = tk.Entry(root)
    day_label = tk.Label(root, text="Day", font=("Helvetica", 12))
    day_entry = tk.Entry(root)

    search_button = tk.Button(root, text="Search", font=("Helvetica", 12, "bold"), width=10, height=1, command=search_games)

    results_text = tk.Text(root, wrap=tk.WORD, height=15, width=60)

    title_label.grid(row=0, column=0, columnspan=4, pady=20)
    subtitle_label.grid(row=1, column=0, columnspan=4, pady=0)
    credits_label.grid(row=2, column=0, columnspan=4, pady=0)
    instructions1_label.grid(row=3, column=0, columnspan=4, pady=20)
    month_label.grid(row=5, column=0, padx=10, pady=10)
    month_entry.grid(row=5, column=1, padx=10, pady=10)
    day_label.grid(row=5, column=2, padx=10, pady=10)
    day_entry.grid(row=5, column=3, padx=10, pady=10)
    search_button.grid(row=6, column=0, columnspan=4, padx=0, pady=0)
    results_text.grid(row=7, column=0, columnspan=4, padx=10, pady=10)


    # Tkinter windows execution
    root.mainloop()

if __name__ == "__main__":
    main()
