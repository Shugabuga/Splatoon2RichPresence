#!/usr/bin/env python3

# If you are reading this, my condolences.
# This tool is licensed under MIT.

from core import rpc
import time, tkinter, requests
from tkinter import *
from tkinter import messagebox

print("\033[95mSplatoon 2 Rich Presence (for Discord)\033[0m")
print("\033[95mCreated by HeyItsShuga - Data from splatoon2.ink\033[0m")
print("")
client_id = '422151392338378753'

rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("\033[92mRPC connection successful.\033[0m")

top = tkinter.Tk()
top.configure(background="#2C2F33")
top.resizable(width=False, height=False)
top.geometry("500x300")
top.wm_title="Splatoon 2 RPC"
top.title="Splatoon 2 RPC"

titleFrame = Frame(top, bg="#2C2F33")
titleFrame.pack(side="left", fill="both", expand=False)

label = Label(titleFrame, fg="#ffffff", bg="#2C2F33", text="Splatoon 2 Rich Presence", font="Splatoon1 25")
label.grid(row=0, column=0)
sublabel = Label(titleFrame, fg="#ffffff", bg="#2C2F33", text="for Discord", font="Splatoon1 14")
sublabel.grid(row=0, column=1)

titleFrame.place(x=15,y=5)


# This function is where the Rich Presence is processed.
def loop(lastMap, start_time):
    txt = open("core/map.txt", "r") 
    mapData = txt.read().split("|")
    currentMap = mapData[0]
    modeID = mapData[1]
    mode = mapData[2]
    icon = currentMap.lower().replace(" ","").replace("'","")

    if(modeID == "r"):
        modeCat = "Ranked"
    elif(modeID == "l"):
        modeCat = "League"
    elif(modeID == "tw"):
        modeCat = "Turf War"
    elif(modeID == "sr"):
        modeCat = "Salmon Run"
    else:
        modeCat = "Unknown"


    if(icon == "lobby"):
        icon = "logo"
    if(currentMap != lastMap):
            start_time = time.time()
            print("")
            print("\033[94mNew Map: " + currentMap + "\033[0m")
            # print("\033[94mIcon ID: " + icon + "\033[0m")
            print("\033[94mMode: " + mode + " (" + modeCat + ")\033[0m")
    activity = {
        "state": "Mode: " + mode,
        "details": "Map: " + currentMap,
        "timestamps": {
            "start": start_time
        },
        "assets": {
            "small_text": modeCat,
            "small_image": modeID,
            "large_text": currentMap,
            "large_image": icon
        }
    }
    rpc_obj.set_activity(activity)

    label.after(1000, lambda:loop(currentMap, start_time))
    # loop()

def map(name, modeID, modeStr):
    txt = open("core/map.txt", "w")
    txt.write(name + "|" + modeID + "|" + modeStr) 


autoRun = Button(top, text = "test", command=loop("",time.time()))

api = requests.get("https://splatoon2.ink/data/schedules.json").json()
salmonAPI = requests.get("https://splatoon2.ink/data/coop-schedules.json").json()

turfFrame = Frame(top, bg="#2C2F33")
turfFrame.pack(side="left", fill="both", expand=False)

TW = Label(turfFrame, font="Splatoon1", bg="#2C2F33", fg="#ffffff", text = "Turf War: ")
TW.grid(row=0, column=0)

A = Button(turfFrame, font="Splatoon2", highlightbackground="#2C2F33", text = api['regular'][0]['stage_a']['name'], command=lambda:map(api['regular'][0]['stage_a']['name'],"tw","Turf War"))
A.grid(row=0, column=1)

B = Button(turfFrame, font="Splatoon2", highlightbackground="#2C2F33", text = api['regular'][0]['stage_b']['name'], command=lambda:map(api['regular'][0]['stage_b']['name'],"tw","Turf War"))
B.grid(row=0, column=2)

turfFrame.place(x=15,y=70)


rankFrame = Frame(top, bg="#2C2F33")
rankFrame.pack(side="left", fill="both", expand=False)

RA = Label(rankFrame, font="Splatoon1", bg="#2C2F33", fg="#ffffff", text = api['gachi'][0]['rule']['name'] + " (Ranked): ")
RA.grid(row=0, column=0)

C = Button(rankFrame, font="Splatoon2", highlightbackground="#2C2F33", text = api['gachi'][0]['stage_a']['name'], command=lambda:map(api['gachi'][0]['stage_a']['name'],"r",api['gachi'][0]['rule']['name']))
C.grid(row=0, column=1)

D = Button(rankFrame, font="Splatoon2", highlightbackground="#2C2F33", text = api['gachi'][0]['stage_b']['name'], command=lambda:map(api['gachi'][0]['stage_b']['name'],"r",api['gachi'][0]['rule']['name']))
D.grid(row=0, column=2)

rankFrame.place(x=15,y=120)


legFrame = Frame(top, bg="#2C2F33")
legFrame.pack(side="left", fill="both", expand=False)

LG = Label(legFrame, font="Splatoon1", bg="#2C2F33", fg="#ffffff", text = api['league'][0]['rule']['name'] + " (League): ")
LG.grid(row=0, column=0)

E = Button(legFrame, font="Splatoon2", highlightbackground="#2C2F33", text = api['league'][0]['stage_a']['name'], command=lambda:map(api['league'][0]['stage_a']['name'],"l",api['league'][0]['rule']['name']))
E.grid(row=0, column=1)

F = Button(legFrame, font="Splatoon2", highlightbackground="#2C2F33", text = api['league'][0]['stage_b']['name'], command=lambda:map(api['league'][0]['stage_b']['name'],"l",api['league'][0]['rule']['name']))
F.grid(row=0, column=2)

legFrame.place(x=15,y=170)


salmonFrame = Frame(top, bg="#2C2F33")
salmonFrame.pack(side="left", fill="both", expand=False)

LG = Label(salmonFrame, font="Splatoon1", bg="#2C2F33", fg="#ffffff", text = "Salmon Run: ")
LG.grid(row=0, column=0)

G = Button(salmonFrame, font="Splatoon2", highlightbackground="#2C2F33", text = salmonAPI['details'][0]['stage']['name'], command=lambda:map(salmonAPI['details'][0]['stage']['name'],"sr","Salmon Run"))
G.grid(row=0, column=1)

salmonFrame.place(x=15,y=220)


attr = Label(top, fg="#99AAB5", bg="#2C2F33", text="Created by HeyItsShuga • Data from splatoon2.ink", font="Splatoon2 20")
attr.place(x=15,y=250)


top.mainloop()