from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class PageLimitPair:
    limit: Optional[int] = None
    page: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PageLimitPair':
        assert isinstance(obj, dict)
        limit = from_union([from_int, from_none], obj.get("limit"))
        page = from_union([from_int, from_none], obj.get("page"))
        return PageLimitPair(limit, page)

    def to_dict(self) -> dict:
        result: dict = {}
        result["limit"] = from_union([from_int, from_none], self.limit)
        result["page"] = from_union([from_int, from_none], self.page)
        return result


@dataclass
class PaginationLinks:
    first: Optional[PageLimitPair] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PaginationLinks':
        assert isinstance(obj, dict)
        first = from_union([PageLimitPair.from_dict, from_none], obj.get("first"))
        return PaginationLinks(first)

    def to_dict(self) -> dict:
        result: dict = {}
        result["first"] = from_union([lambda x: to_class(PageLimitPair, x), from_none], self.first)
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
class AlbumsPage:
    links: Optional[PaginationLinks] = None
    meta: Optional[PageMetadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AlbumsPage':
        assert isinstance(obj, dict)
        links = from_union([PaginationLinks.from_dict, from_none], obj.get("links"))
        meta = from_union([PageMetadata.from_dict, from_none], obj.get("meta"))
        return AlbumsPage(links, meta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["links"] = from_union([lambda x: to_class(PaginationLinks, x), from_none], self.links)
        result["meta"] = from_union([lambda x: to_class(PageMetadata, x), from_none], self.meta)
        return result


@dataclass
class Data:
    albums: Optional[AlbumsPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        albums = from_union([AlbumsPage.from_dict, from_none], obj.get("albums"))
        return Data(albums)

    def to_dict(self) -> dict:
        result: dict = {}
        result["albums"] = from_union([lambda x: to_class(AlbumsPage, x), from_none], self.albums)
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
class AlbumsLinkMeta:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AlbumsLinkMeta':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return AlbumsLinkMeta(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def albums_link_meta_from_dict(s: Any) -> AlbumsLinkMeta:
    return AlbumsLinkMeta.from_dict(s)


def albums_link_meta_to_dict(x: AlbumsLinkMeta) -> Any:
    return to_class(AlbumsLinkMeta, x)
