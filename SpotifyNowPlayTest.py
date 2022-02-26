#/bin/env python3
from pythonosc import udp_client
from SwSpotify import spotify
import time
import random
client_osc = udp_client.SimpleUDPClient("127.0.0.1",9000)
#Spotify
while True:
    try:
        song = spotify.song()
    except Exception as e:
        client_osc.send_message("/avatar/parameters/ismusic",0)
        print("Beep-boop, Toaster doesn't hear music")
        time.sleep(1.0)
    else:
        client_osc.send_message("/avatar/parameters/ismusic",1)
        print("beep-boop, Toaster hears: "+song)
        songlen=len(song)
        #for x in songlen:
        #    print(ord(song[x]))
        #else:
        time.sleep(1.0)
