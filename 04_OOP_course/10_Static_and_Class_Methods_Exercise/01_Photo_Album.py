from math import ceil
from typing import List


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE: int = 4
    DASHES_COUNT: int = 11
    SYMBOL_FOR_LINE: str = "-"

    def __init__(self, pages: int):
        self.pages = pages  # (empty matrix) representing the album with its pages where you should put the photos
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        """creates a new instance of PhotoAlbum. Note: Each page can contain 4 photos"""
        pages = ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        """adds the photo in the first possible page and slot"""
        for page_num in range(self.pages):
            if len(self.photos[page_num]) < self.MAX_PHOTOS_PER_PAGE:
                slot = len(self.photos[page_num]) + 1
                self.photos[page_num].append(label)

                return f"{label} photo added successfully on page {page_num + 1} slot {slot}"

        else:
            return "No more free slots"

    def display(self):
        result = [self.SYMBOL_FOR_LINE * self.DASHES_COUNT]
        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.SYMBOL_FOR_LINE * self.DASHES_COUNT)

        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
