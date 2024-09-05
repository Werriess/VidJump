from tkinter import *
from youtube_transcript_api import YouTubeTranscriptApi
from tkhtmlview import HTMLLabel
import customtkinter
from bs4 import BeautifulSoup 

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.iconbitmap('./icons/yt_logo.ico')
root.title("VidJump")
root.geometry('700x500')

txtOne = customtkinter.CTkEntry(master=root, width=300, placeholder_text="Paste in your YouTube link")
txtOne.grid(column=0, row=0, pady="10")

txtTwo = customtkinter.CTkEntry(master=root, width=300, placeholder_text="What word are you searching for?")
txtTwo.grid(column=0, row=1)

frm = customtkinter.CTkFrame(master=root, width=200, height=200)
frm.grid(column=0, row=4, columnspan=3, pady=10, padx=20)

frame_lbl = HTMLLabel(frm, html="")
frame_lbl.pack(fill=BOTH, expand=True)

def on_clicked_fetched():
    searchlink = txtOne.get()
    searchlinksub = searchlink.split('?v=')
    searchID = searchlinksub[1] 
    
    searchText = txtTwo.get()
    result = get_timestamped_video(searchText, searchID)
    frame_lbl.set_html(result)

def get_timestamped_video(searchText, searchID):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(searchID)
        result = []
        found = False
        
        for entry in transcript:
            if searchText.lower() in entry['text'].lower():
                found = True
                timestamp = entry['start']
                url = f"https://www.youtube.com/watch?v={searchID}&t={int(timestamp)}s"
                result.append(
                    f'''
                    <p style="font-family: Arial, sans-serif; color: #333; font-size: 10px; margin-bottom: 10px;">
                        Found "<strong>{searchText}</strong>" at 
                        <a href="{url}" style="color: red; text-decoration: none;">{timestamp} seconds</a>:
                        <br>
                        <span style="color: #555;">{entry["text"]}</span>
                    </p>
                    '''
                )
        
        if not found:
            result = [f'<p style="font-family: Arial, sans-serif; color: #333; font-size: 10px">"{searchText}" not found in the transcript.</p>']
        
        return "<br>".join(result)
    
    except Exception as e:
        return f'<p style="font-family: Arial, sans-serif; color: #d9534f;">An error occurred: {e}</p>'

def extract_hrefs(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.find_all('a', href=True)]

def save_to_file(data, searchData):
    with open("Yt_data.txt", "a") as f:
        f.write(f"--------{searchData.upper()}--------\n")
        f.write(f"{data}\n")

def on_clicked_save():
    searchlink = txtOne.get()
    searchlinksub = searchlink.split('?v=')
    searchID = searchlinksub[1] 
    
    searchText = txtTwo.get()
    result = get_timestamped_video(searchText, searchID)
    
    hrefs = extract_hrefs(result)
    data_to_save = "\n".join(hrefs)
    
    save_to_file(data_to_save, searchText)

btn = customtkinter.CTkButton(master=root, text="Fetch", command=on_clicked_fetched, fg_color="red", hover_color="#cc0000")
btn.grid(column=1, row=0)

btn = customtkinter.CTkButton(master=root, text="Save data", command=on_clicked_save, fg_color="red", hover_color="#cc0000")
btn.grid(column=1, row=1)

root.mainloop()
