import datetime
import os
import re

from mtd.track_info import *


def write_in_file(filename, container, is_album=True):
    with open(filename, "a", encoding="utf-8") as f:
        rows = container.values.tolist()
        if is_album:
            f.write("\nArtist - Album\n\n")
        else:
            f.write("\nArtist - Song\n\n")

        for row in rows:
            if is_album:
                f.write(f"{row[0]} - {row[1]}  {row[2]} Songs\n")
            else:
                f.write(f"{row[1]} - {row[0]}\n")


def run(filename_path):
    date = datetime.datetime
    file_name = re.split(r"[\./]", filename_path)[-2]
    write_to_file = f"{file_name}_{str(date.today().strftime("%d%m%Y%H%M%S"))}.txt"
    is_file = os.path.isfile(write_to_file)

    tracks = get_new_dataframe(filename_path)
    if check_soundtrack(tracks):
        write_in_file(write_to_file, tracks, False)
    else:
        albums = get_count_of_songs_in_album(tracks)
        songs = get_list_of_songs_by_artist(tracks, albums)
        write_in_file(write_to_file, albums)
        write_in_file(write_to_file, songs, False)
