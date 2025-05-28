import pandas as pd
from functools import partial


def remove_after_separator(name: str, separator: str) -> str:
    separator = ","
    result = name.split(separator, 1)[0]

    return result


def get_new_dataframe(filename):
    original_df = pd.read_csv(filename)

    new_df = original_df[["Song", "Artist", "Album"]].sort_values(by="Artist")
    return new_df


def check_soundtrack(dataframe) -> bool:
    total_entries_length = len(dataframe)
    first_entry_album = dataframe["Album"][0]
    first_entry_album = remove_after_separator(first_entry_album, ",")
    album_entries = dataframe["Album"].str.contains(first_entry_album, regex=False)
    album_entries_length = len(dataframe[album_entries])
    percentage = album_entries_length / total_entries_length * 100
    # print(f"Percentage: {int(percentage)}%")

    if percentage >= 75:
        print(f"Percentage: {int(percentage)}%")
        return True

    first_entry_artist = dataframe["Artist"][0]
    first_entry_artist = remove_after_separator(first_entry_artist, ",")
    artist_entries = dataframe["Artist"].str.contains(first_entry_artist, regex=False)
    artist_entries_length = len(dataframe[artist_entries])

    percentage = artist_entries_length / total_entries_length * 100
    # print(f"Percentage: {int(percentage)}%")

    if percentage >= 75:
        print(f"Percentage: {int(percentage)}%")
        return True

    return False


def get_count_of_songs_in_album(dataframe, upper_limit=4):
    tmp_df = dataframe[["Artist", "Album"]].astype(str)
    remove_separator = partial(remove_after_separator, separator=",")

    tmp_df["Artist"] = tmp_df["Artist"].apply(remove_separator)
    # tmp_df["Artist"] = tmp_df["Artist"].apply(remove_after_separator)
    new_df = (
        tmp_df[["Artist", "Album"]]
        .groupby(["Artist", "Album"], as_index=False)
        .filter(lambda x: len(x) >= upper_limit)
        .value_counts()
        .reset_index()
    )
    # TODO order by artist name

    return new_df


def get_list_of_songs_by_artist(dataframe, albums):
    album_list = albums["Album"].values.tolist()

    songs = dataframe[~dataframe["Album"].isin(album_list)]
    return songs
