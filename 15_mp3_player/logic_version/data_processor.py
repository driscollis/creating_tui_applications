# data_processor.py

import eyed3
import pathlib


def get_mp3(path: pathlib.Path) -> tuple:
    mp3 = eyed3.load(str(path))
    track_num = mp3.tag.track_num.count
    title = mp3.tag.title
    length = f"{int(mp3.info.time_secs // 60)}:{int(mp3.info.time_secs % 60):02d}"
    artist = mp3.tag.artist
    album = mp3.tag.album
    return album, track_num, title, length, artist, str(path)


def process_mp3s(path: pathlib.Path) -> list[str]:
    """
    Process the MP3 file or folder and turn it into a list of lists
    """
    mp3s = []

    mp3s.append(["Album", "#", "Title", "Length", "Artist", "Location"])

    if path.is_file():
        mp3s.append(list(get_mp3(path)))
    elif path.is_dir():
        for mp3_path in path.glob("*.mp3"):
            mp3s.append(list(get_mp3(mp3_path)))
    return mp3s
