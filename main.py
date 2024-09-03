from tkinter import *
from youtube_transcript_api import YouTubeTranscriptApi
from tkhtmlview import HTMLLabel

root = Tk()
root.title("Welcome Jump to Timestamp")
root.geometry('700x500')

lbl = Label(root, text="Paste in your YouTube link?")
lbl.grid(column=0, row=0)

txtOne = Entry(root, width=30)
txtOne.grid(column=1, row=0)

lbl = Label(root, text="What word are you searching for?")
lbl.grid(column=0, row=1)

txtTwo = Entry(root, width=30)
txtTwo.grid(column=1, row=1)

frm = Frame(root)
frm.grid(column=0, row=4, columnspan=3, pady=10)

frame_lbl = HTMLLabel(frm, html="")
frame_lbl.pack(fill=BOTH, expand=True)

def on_clicked():
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
                        <a href="{url}" style="color: #1a73e8; text-decoration: none;">{timestamp} seconds</a>:
                        <br>
                        <span style="color: #555;">{entry["text"]}</span>
                    </p>
                    '''
                )
        
        if not found:
            result = [f'<p style="font-family: Arial, sans-serif; color: #333;">"{searchText}" not found in the transcript.</p>']
        
        return "<br>".join(result)
    
    except Exception as e:
        return f'<p style="font-family: Arial, sans-serif; color: #d9534f;">An error occurred: {e}</p>'


btn = Button(root, text="Fetch", fg="black", command=on_clicked)
btn.grid(column=3, row=1)

root.mainloop()
