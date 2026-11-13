import pytest
from library_item import LibraryItem

# I'm testing the LibraryItem class to make sure it works correctly

def test_item_name():  # I'm testing that the name is stored correctly
    item = LibraryItem("What a Wonderful World", "Louis Armstrong", 5)
    assert item.name == "What a Wonderful World"

def test_item_artist():  # I'm testing that the artist is stored correctly
    item = LibraryItem("What a Wonderful World", "Louis Armstrong", 5)
    assert item.artist == "Louis Armstrong"

def test_item_rating():  # I'm testing that the rating is stored correctly
    item = LibraryItem("What a Wonderful World", "Louis Armstrong", 5)
    assert item.rating == 5

def test_item_play_count():  # I'm testing that play count starts at 0
    item = LibraryItem("What a Wonderful World", "Louis Armstrong", 5)
    assert item.play_count == 0

def test_increment_play_count():  # I'm testing that play count increases by 1
    item = LibraryItem("What a Wonderful World", "Louis Armstrong", 5)
    item.play_count += 1
    assert item.play_count == 1