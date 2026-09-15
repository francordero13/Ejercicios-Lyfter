def read_songs(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        songs = file.readlines()

    songs = [song.strip() for song in songs]

    return songs


def filter_songs(songs):
    songs.sort()

    return songs


def save_songs(songs, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for song in songs:
            file.write(song + "\n")


input_file = r"C:\Users\franc\Downloads\songs.txt"
output_file = r"C:\Users\franc\Downloads\canciones_ordenadas.txt"

songs = read_songs(input_file)

songs_filter = filter_songs(songs)

save_songs(songs_filter, output_file)

print("Las canciones fueron ordenadas y guardadas.")