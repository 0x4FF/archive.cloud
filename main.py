from requests import get
from json import loads
from colorama import Fore
from sys import argv
from os import system
from time import sleep
import argparse

id = ""
id2 = ""


def get_tracks():
  tracks_request = get(
    f"https://api-mobile.soundcloud.com/users/{urn}/tracks/posted?client_id={id}&limit=200"
  )
  tracks = loads(tracks_request.text)
  count = 0
  for track in tracks['collection']:
    with open(f"results.txt", "a") as f:
      count += 1
      try:
        f.write(f"""
=====================================================
Title: {tracks['collection'][count]['track']['title']}

Created: {tracks['collection'][count]['track']['created_at']}
Uploaded: {tracks['collection'][count]['track']['published_at']}

Duration: {tracks['collection'][count]['track']['duration']}

Likes: {tracks['collection'][count]['track']['_embedded']['stats']['likes_count']}
Plays: {tracks['collection'][count]['track']['_embedded']['stats']['playback_count']}
Comments: {tracks['collection'][count]['track']['_embedded']['stats']['comments_count']}
Reposts: {tracks['collection'][count]['track']['_embedded']['stats']['reposts_count']}

Sharing: {tracks['collection'][count]['track']['sharing']}

WaveForm: {tracks['collection'][count]['track']['waveform_url']}
PermLink: {tracks['collection'][count]['track']['permalink_url']}

Description: {tracks['collection'][count]['track']['description']}


========================================================
        
""")
      except KeyError:
        pass
      except IndexError:
        print("results.txt was made")
      finally:
        pass


def resolver():
  global urn
  target_url = argv[2]
  try:
    get_track = get(
      f"https://api-widget.soundcloud.com/resolve?url={target_url}&format=json&client_id={id2}"
    )
    track_string = loads(get_track.text)
    urn = track_string['urn']
    get_tracks()
  except KeyError:
    print("Endpoint bugged in resolving URL, try again")
    sleep(3)
    system("clear")
    sleep(2)
    main()
    
    
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-u", help="Set Target URL")
  cli_args = parser.parse_args()

  if cli_args.u:
    print(f"""{Fore.RED}

╔═╗╦═╗╔═╗╦ ╦╦╦  ╦╔═╗ ╔═╗╦  ╔═╗╦ ╦╔╦╗
╠═╣╠╦╝║  ╠═╣║╚╗╔╝║╣  ║  ║  ║ ║║ ║ ║║
╩ ╩╩╚═╚═╝╩ ╩╩ ╚╝ ╚═╝o╚═╝╩═╝╚═╝╚═╝═╩╝
{Fore.RESET}MOTD: get dem losts    Developer: github.com/0x4FF       
""")
    resolver()


if __name__ == "__main__":
  main()
