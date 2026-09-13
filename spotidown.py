import platform
import subprocess
import sys
import os
import urllib.request
import zipfile
import shutil

def instalador_pack_all(pacotea):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pacotea])


def instalador_pack_lin(pacotel):
    subprocess.check_call(["sudo", "apt", "install", "-y", pacotel])


def instalar_ffmpeg():
    if not shutil.which("ffmpeg"):
        ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

        ffmpeg_zip = "ffmpeg.zip"
        pasta_destino = os.path.join(os.getcwd(), "ffmpeg")

        if os.path.exists(os.path.join(pasta_destino, "bin", "ffmpeg.exe")):
            print("FFmpeg is already installed✅​.")
            return
    
        print("downloading​🌐​FFmpeg...")

        urllib.request.urlretrieve(ffmpeg_url, ffmpeg_zip)

        print("extracting​📂​FFmpeg")

        with zipfile.ZipFile(ffmpeg_zip, "r") as zip_ref:
            zip_ref.extractall(pasta_destino)

        past_bin = None

        for raiz, pastas, arquivos in os.walk(pasta_destino):
            if "ffmpeg.exe" in arquivos:
                past_bin = raiz
                break

        if past_bin is None:
            print("Could not find ffmpeg.exe.")
            return

        os.environ["PATH"] += os.pathsep + past_bin
        print("FFmpeg successfully installed✅​!!")

        os.remove(ffmpeg_zip)
    else:
        return 0

def instalar_spotdl():
    sist = platform.system()

    if sist == "Linux":
        instalador_pack_lin("ffmpeg")
        instalador_pack_all("spotdl")

    elif sist == "Windows":
        instalar_ffmpeg()
        instalador_pack_all("spotdl")

    else:
        print("your system is not supported​🔧​!!")

sist = platform.system()
if sist == "Windows":
    print("windows detected🪟​")
    instalar_spotdl

elif sist == "Linux":
    print("linux detected🐧​")
    instalar_spotdl

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def baixar_play():

    clear()

    print("paste your link here💽​!!")
    link = input(": ").strip()

    validaçao = "/playlist/" and "/open.spotify.com" in link

    if validaçao == True:

        past_m = "spotify_plalist"
        os.makedirs(past_m, exist_ok=True)

        comando = f'spotdl download "{link}" --output "{past_m}/%(artist)s - %(title)s.%(ext)s"'

        print(f"\n playlist download started {past_m}🗂️​...\n")

        try:
            subprocess.run(comando, shell=True, check=True)
            print("\n download done successfully🟢​")
        except subprocess.CalledProcessError as e:
            print(f"\n Erro : {e}")
    else:
        print("your link is not valid❌​")
        sys.exit

if __name__ == "__main__":
    print("installing all program dependencies⚙️​...")

    instalar_spotdl()
    instalar_ffmpeg()
    baixar_play()
