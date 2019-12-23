import json

import requests


class Track:
    def __init__(self, name, alias, artist, album, duration):
        self.name = name
        self.alias = alias
        self.artist = artist
        self.album = album
        self.duration = duration


class Playlist:
    def __init__(self, name, description, tags, tracks):
        self.name = name
        self.description = description
        self.tags = tags
        self.tracks = tracks


class Album:
    def __init__(self, name, img_url):
        self.name = name
        self.img_url = img_url


BASE_URL = "http://localhost:3000/"
UID = "35708560"
EXPORT_FILE = "liuconen_playlist.json"


def obj_dict(obj):
    return obj.__dict__


def get_user_playlist_ids(uid):
    dicts = json.loads(requests.get(f"{BASE_URL}user/playlist?uid={uid}").text)
    return list(
        map(
            lambda x: x["id"],
            filter(lambda x: str(x["creator"]["userId"]) == UID, dicts["playlist"])
        )
    )


def get_playlist_tracks(json_dicts):
    return list(
        map(lambda x: Track(
            x["name"],
            x["alia"],
            list(map(lambda y: y["name"], x["ar"])),
            Album(x["al"]["name"], x["al"]["picUrl"]),
            None
        ), json_dicts["tracks"])
    )


def export_playlist_to_json(playlist):
    json_string = json.dumps(playlist, default=obj_dict, indent=2, ensure_ascii=False)
    with open(EXPORT_FILE, 'w', encoding="utf-8") as outfile:
        outfile.write(json_string)


if __name__ == '__main__':
    playlist_ids = get_user_playlist_ids(UID)
    play_lists = []
    for p in playlist_ids:
        detail = json.loads(requests.get(f"{BASE_URL}playlist/detail?id={p}").text)["playlist"]
        p = Playlist(detail["name"], detail["description"], detail["tags"], get_playlist_tracks(detail))
        play_lists.append(p)
    export_playlist_to_json(play_lists)
