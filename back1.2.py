import platform
import subprocess
import sys
import os
import urllib.request
import zipfile
import shutil

def instalador_pack_win(pacotew):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pacotew])


def instalador_pack_lin(pacotel):
    subprocess.check_call(["sudo", "apt", "install", "-y", pacotel])


def instalar_ffmpeg_windows():
    if not shutil.which("ffmpeg"):
        ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

        ffmpeg_zip = "ffmpeg.zip"
        pasta_destino = os.path.join(os.getcwd(), "ffmpeg")

        if os.path.exists(os.path.join(pasta_destino, "bin", "ffmpeg.exe")):
            print("FFmpeg já está instalado.")
            return
    
        print("tentando baixar o FFmpeg...")

        urllib.request.urlretrieve(ffmpeg_url, ffmpeg_zip)

        print("Extraindo FFmpeg")

        with zipfile.ZipFile(ffmpeg_zip, "r") as zip_ref:
            zip_ref.extractall(pasta_destino)

        past_bin = None

        for raiz, pastas, arquivos in os.walk(pasta_destino):
            if "ffmpeg.exe" in arquivos:
                past_bin = raiz
                break

        if past_bin is None:
            print("Não foi possível encontrar o ffmpeg.exe.")
            return

        os.environ["PATH"] += os.pathsep + past_bin
        print("FFmpeg instalado com sucesso!!")

        os.remove(ffmpeg_zip)
    else:
        return 0

def instalar_spotdl():
    sist = platform.system()

    if sist == "Linux":
        instalador_pack_lin("ffmpeg")
        instalador_pack_win("spotdl")

    elif sist == "Windows":
        instalar_ffmpeg_windows()
        instalador_pack_win("spotdl")

    else:
        print("seu sistema nao é surportado!!")

sist = platform.system()
if sist == "Windows":
    print("windows detectado.")
    instalar_spotdl

elif sist == "Linux":
    print("linux detectado")
    instalar_spotdl

def baixar_play():
    print("cole seu link aqui!!")
    link = input(": ").strip()



    validaçao = "/playlist/" and "/open.spotify.com" in link

    if validaçao == True:

        past_m = "spotify_plalist"
        os.makedirs(past_m, exist_ok=True)

        comando = f'spotdl download "{link}" --output "{past_m}/%(artist)s - %(title)s.%(ext)s"'

        print(f"\n iniciado o download da playlist {past_m}...\n")

        try:
            subprocess.run(comando, shell=True, check=True)
            print("\n Download concluído")
        except subprocess.CalledProcessError as e:
            print(f"\n Erro : {e}")

if __name__ == "__main__":
    print("Iniciando instalação do que precisa...")

    instalar_spotdl()
    instalar_ffmpeg_windows()
    baixar_play()