from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class DataPhoto:
    thumbnail_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataPhoto':
        assert isinstance(obj, dict)
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnailUrl"))
        return DataPhoto(thumbnail_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["thumbnailUrl"] = from_union([from_str, from_none], self.thumbnail_url)
        return result


@dataclass
class PageMetadata:
    total_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PageMetadata':
        assert isinstance(obj, dict)
        total_count = from_union([from_int, from_none], obj.get("totalCount"))
        return PageMetadata(total_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalCount"] = from_union([from_int, from_none], self.total_count)
        return result


@dataclass
class PhotosPage:
    meta: Optional[PageMetadata] = None
    data: Optional[List[Optional[DataPhoto]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PhotosPage':
        assert isinstance(obj, dict)
        meta = from_union([PageMetadata.from_dict, from_none], obj.get("meta"))
        data = from_union([lambda x: from_list(lambda x: from_union([DataPhoto.from_dict, from_none], x), x), from_none], obj.get("data"))
        return PhotosPage(meta, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["meta"] = from_union([lambda x: to_class(PageMetadata, x), from_none], self.meta)
        result["data"] = from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(DataPhoto, x), from_none], x), x), from_none], self.data)
        return result


@dataclass
class Album:
    title: Optional[str] = None
    id: Optional[str] = None
    photos: Optional[PhotosPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Album':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        id = from_union([from_str, from_none], obj.get("id"))
        photos = from_union([PhotosPage.from_dict, from_none], obj.get("photos"))
        return Album(title, id, photos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["id"] = from_union([from_str, from_none], self.id)
        result["photos"] = from_union([lambda x: to_class(PhotosPage, x), from_none], self.photos)
        return result


@dataclass
class PhotoPhoto:
    id: Optional[str] = None
    thumbnail_url: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    album: Optional[Album] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PhotoPhoto':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnailUrl"))
        title = from_union([from_str, from_none], obj.get("title"))
        url = from_union([from_str, from_none], obj.get("url"))
        album = from_union([Album.from_dict, from_none], obj.get("album"))
        return PhotoPhoto(id, thumbnail_url, title, url, album)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["thumbnailUrl"] = from_union([from_str, from_none], self.thumbnail_url)
        result["title"] = from_union([from_str, from_none], self.title)
        result["url"] = from_union([from_str, from_none], self.url)
        result["album"] = from_union([lambda x: to_class(Album, x), from_none], self.album)
        return result


@dataclass
class Data:
    photo: Optional[PhotoPhoto] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        photo = from_union([PhotoPhoto.from_dict, from_none], obj.get("photo"))
        return Data(photo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["photo"] = from_union([lambda x: to_class(PhotoPhoto, x), from_none], self.photo)
        return result


@dataclass
class Error:
    message: str

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        message = from_str(obj.get("message"))
        return Error(message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_str(self.message)
        return result


@dataclass
class PhotoAlbumPhotosMeta:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PhotoAlbumPhotosMeta':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return PhotoAlbumPhotosMeta(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def photo_album_photos_meta_from_dict(s: Any) -> PhotoAlbumPhotosMeta:
    return PhotoAlbumPhotosMeta.from_dict(s)


def photo_album_photos_meta_to_dict(x: PhotoAlbumPhotosMeta) -> Any:
    return to_class(PhotoAlbumPhotosMeta, x)
