import sys
import os
import yt_dlp
import re
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from colorama import Fore, init

init(autoreset=True)
def Main_Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + fr"""___________             __     _____.___.              _________                       __________.__       .__     __   
\_   _____/_ __   ____ |  | __ \__  |   | ____  __ __  \_   ___ \  ____ ______ ___.__. \______   \__| ____ |  |___/  |_ 
 |    __)|  |  \_/ ___\|  |/ /  /   |   |/  _ \|  |  \ /    \  \/ /  _ \\____ <   |  |  |       _/  |/ ___\|  |  \   __\
 |     \ |  |  /\  \___|    <   \____   (  <_> )  |  / \     \___(  <_> )  |_> >___  |  |    |   \  / /_/  >   Y  \  |  
 \___  / |____/  \___  >__|_ \  / ______|\____/|____/   \______  /\____/|   __// ____|  |____|_  /__\___  /|___|  /__|  
     \/              \/     \/  \/                             \/       |__|   \/              \/  /_____/      \/    
    """ + Fore.GREEN +  """[""" + Fore.WHITE + """ 1 """ + Fore.GREEN + """]""" + Fore.GREEN + """ Youtube Downloader""" + Fore.RED + """               ⠀⠀⠀⠀⠀⠀              """ + Fore.RED +  """          ⠀⠀ ⣠⣿⣋⣀⣀⣀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀
    """ + Fore.GREEN +  """[""" + Fore.WHITE + """ 2 """ + Fore.GREEN + """]""" + Fore.GREEN + """ Tik-Tok Downloader""" + Fore.RED + """                                         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⡤⠤⠤⢤⡤
    """ + Fore.RED + """[ 00 ] Exit""" + Fore.RED + """                                                      ⣿⣿⣿⠿⠟⠉⠉⠀⣹⣿⣋⣻⣿⡇⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠈⠀⠀⠀⠀⠀
                                                                     ⠈⠉⠀⠀⠀⠀⠀⣴⡿⠁⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   """ + Fore.BLUE + """Created by:""" + Fore.WHITE +  """ XFM9""" + Fore.RED + """
        ⠀⠀⠀⠀⠀⠀⠀⠀                                                             ⠁⠀⠀⠘⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    
    Com = str(input("Enter ID: "))
    if Com == "00":
        print(Fore.GREEN + "Bye!")
        sys.exit(0)
    else:
        if Com in Menu_Com:
            Menu_Com[Com]()
            Com = None
        else:
            print(Fore.RED + "Invalid ID")

def Youtube_Downloader():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + fr"""_____.___.              __       ___.            ________                      .__                    .___            
\__  |   | ____  __ ___/  |_ __ _\_ |__   ____   \______ \   ______  _  ______ |  |   _________     __| _/___________ 
 /   |   |/  _ \|  |  \   __\  |  \ __ \_/ __ \   |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \
 \____   (  <_> )  |  /|  | |  |  / \_\ \  ___/   |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/
 / ______|\____/|____/ |__| |____/|___  /\___  > /_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   
 \/                                   \/     \/          \/                  \/                \/      \/    \/       """)


    print("")
    print(Fore.GREEN + "[" + Fore.WHITE + " 1 "+ Fore.GREEN + "]" " Install Video")
    print(Fore.GREEN + "[" + Fore.WHITE + " 2 "+ Fore.GREEN + "]" " Install Audio")
    print(Fore.GREEN + "[" + Fore.WHITE + " 3 "+ Fore.GREEN + "]" " Install Thumbnail")
    print(Fore.RED + "[ 00 ] Exit")
    
    print("")
    YD_ID = str(input("Enter ID: "))
    
    if YD_ID not in ("1", "2", "3", "00"):
        print(Fore.RED + "ERROR: Invalid Сhoice")
    else:
        if YD_ID == "00":
            print(Fore.GREEN + "Bye!")
            sys.exit(0)
        
        Link = input("Enter YouTube Link: ")
        

        if YD_ID == "1":
            if "&" in Link:
                Link = Link.split("&")[0]

            info_opts = {
                'quiet': True,
                'no_warnings': True,
                'noplaylist': True,
                'jsruntimes': 'deno'
            }

            with YoutubeDL(info_opts) as ydl:
                info = ydl.extract_info(Link, download=False)
            resolutions = sorted({f['height'] for f in info['formats'] if f.get('height') and f['height'] >= 360})

            print(Fore.GREEN + "\nVideo Resolutions:")
            for x, r in enumerate(resolutions):
                print(Fore.GREEN + f"[{Fore.WHITE} {x} {Fore.GREEN}] {r}p")

            Res = input("Enter ID: ")
            if Res.isdigit():
                Res = int(Res)
                if 0 <= Res < len(resolutions):
                    selected = resolutions[Res]
                    print(Fore.GREEN + f"Selected Resolution: {selected}p")

                    ydl_opts = {
                        'format': f'bestvideo[height={selected}]+bestaudio/best',
                        'merge_output_format': 'webm',
                        'jsruntimes': 'deno',
                        'noplaylist': True,
                    }

                    with YoutubeDL(ydl_opts) as ydl:
                        ydl.download([Link])
                    
                    input("Press Enter to return to menu...")
                    Main_Menu()

                    
                else:
                    print(Fore.RED + "ERROR: Invalid ID")
            else:
                print(Fore.RED + "ERROR: Must be a number")

        elif YD_ID == "2":
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([Link])
            
            input("Press Enter to return to menu...")
            Main_Menu()

        elif YD_ID == "3":
            ydl_opts = {
                'skip_download': True,
                'writethumbnail': True,
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([Link])
            
            input("Press Enter to return to menu...")
            Main_Menu()

def Tik_Tok_Downloader():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + fr"""  _____ _ _       _____     _      ____                      _                 _           
 |_   _(_) | __  |_   _|__ | | __ |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   | | | | |/ /____| |/ _ \| |/ / | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
   | | | |   <_____| | (_) |   <  | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
   |_| |_|_|\_\    |_|\___/|_|\_\ |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|""")
    
    
    print("")
    print(Fore.CYAN + "[" + Fore.WHITE + " 1 "+ Fore.CYAN + "]" " Install Video")
    print(Fore.CYAN + "[" + Fore.WHITE + " 2 "+ Fore.CYAN + "]" " Install Audio")
    print(Fore.RED + "[ 00 ] Exit")
    
    print("")
    TT_ID = str(input("Enter ID: "))
    
    if TT_ID not in ("1", "2", "3", "00"):
        print(Fore.RED + "ERROR: Invalid Сhoice")
    else:
        if TT_ID == "00":
            print(Fore.GREEN + "Bye!")
            sys.exit(0)
            
        Link = input("Enter Tik-Tok Link: ")
        
        if TT_ID == "1":
            ydl_opts = {
                'outtmpl': '%(title)s.%(ext)s'
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([Link])
                
            input("Press Enter to return to menu...")
            Main_Menu()
        
        elif TT_ID == "2":
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": "%(title)s.%(ext)s",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([Link])
            
            input("Press Enter to return to menu...")
            Main_Menu()
    
    

Menu_Com = {"1": Youtube_Downloader, "2": Tik_Tok_Downloader}

if __name__ == "__main__":
    try:
        Main_Menu()
    
    except Exception as e:
        print(Fore.RED + f"\nERROR: {e}")
        sys.exit(1)
    
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nERROR: KeyboardInterrupt")
        sys.exit(0)
    
    except AttributeError:
        print(Fore.MAGENTA + "\nERROR: AttributeError")
        sys.exit(1)
