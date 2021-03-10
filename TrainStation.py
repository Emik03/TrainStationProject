import requests
import tkinter as tk
import json
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# List of stations.
stations = { 'Karlstad':'Ks', 'Arvika': 'Ar' }

def search():
    API_KEY = 'aa916ca49ce741d5bc78df1302631bfd'
    URL = 'https://api.trafikinfo.trafikverket.se/v1.3/data.json'

    # Creates the request.
    request = f"""<REQUEST><LOGIN authenticationkey="{API_KEY}" /><QUERY objecttype="TrainAnnouncement" schemaversion="1.3" orderby="AdvertisedTimeAtLocation"><FILTER><AND><EQ name="ActivityType" value="Avgang" /><EQ name="LocationSignature" value="{stations[state.get()]}" /><OR><AND><GT name="AdvertisedTimeAtLocation" value="$dateadd(07:00:00)" /><LT name="AdvertisedTimeAtLocation" value="$dateadd(12:00:00)" /></AND></OR></AND></FILTER><INCLUDE>AdvertisedTrainIdent</INCLUDE><INCLUDE>AdvertisedTimeAtLocation</INCLUDE><INCLUDE>TrackAtLocation</INCLUDE><INCLUDE>ToLocation</INCLUDE></QUERY></REQUEST>"""

    # This request is sent, we also have to specify that it's XML.
    response = requests.post(URL, data = request, headers = {'Content-Type': 'text/xml'})

    # This retrieves the information sent.
    response_json = json.loads(response.text)
    departures = response_json["RESPONSE"]['RESULT'][0]['TrainAnnouncement']

    # We need to first reenable the text field before editing it.
    txt.config(state="normal")

    # We need to also clear it before we insert text.
    txt.delete(1.0,"end")

    # Writes the list.
    for dep in departures:
        txt.insert(1., dep)
        txt.insert(1., '\n--------------------\n')
    
    # Disables it again, to make sure that it remains readonly.
    txt.config(state="disabled")

def save():
    # Opens a prompt to save a file name.
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Text File', '*.txt'), ('All Files', '*.*')],
    )

    # Prematurely break if the user deselects or cancels the operation. 
    if not filepath:
        return

    # Writes the file and the desired destination.
    with open(filepath, 'w') as output_file:
        text = txt.get(1.0, tk.END)
        output_file.write(text)

# Creates the window.
window = tk.Tk()
window.title(f'Train Station Viewer')
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

# Text field.
txt = tk.Text(window, state='disabled')

# Drop shadows.
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_dropdown = tk.Frame(window, relief=tk.RAISED, bd=2)

# Buttons.
btn_open = tk.Button(fr_buttons, text='Search', command=search)
btn_save = tk.Button(fr_buttons, text='Save as .txt', command=save)

# Dropdown.
state = tk.StringVar()
menu = tk.OptionMenu(window, state, 'Karlstad', 'Avrika')
menu.pack()

# Organises all of the UI elements.
btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)
menu.grid(row=2, column=1, sticky='ew', padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky='ns')
fr_dropdown.grid(row=2, column=1, sticky='ns')
txt.grid(row=0, column=1, sticky='nsew')

window.mainloop()