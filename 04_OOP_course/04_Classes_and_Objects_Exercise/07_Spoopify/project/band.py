from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            current_album = next(filter(lambda a: album_name == a.name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if current_album.published:
            return "Album has been published. It cannot be removed."
        else:
            self.albums.remove(current_album)
            return f"Album {album_name} has been removed."

    def details(self):
        album_details = [album.details() for album in self.albums]
        return f"Band {self.name}\n" + "\n".join(album_details)
