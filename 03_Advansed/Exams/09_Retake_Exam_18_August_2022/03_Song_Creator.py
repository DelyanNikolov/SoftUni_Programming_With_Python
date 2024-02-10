def add_songs(*song_data):
    result = []
    song_collection = {}

    for song, lyrics in song_data:
        if song not in song_collection:
            song_collection[song] = lyrics
        else:
            song_collection[song] += lyrics

    for song_name, collected_lyrics in song_collection.items():
        result.append(f"- {song_name}")
        for line in collected_lyrics:
            result.append(f"{line}")

    return '\n'.join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
