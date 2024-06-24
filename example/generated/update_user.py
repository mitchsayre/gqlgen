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
    last: Optional[PageLimitPair] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PaginationLinks':
        assert isinstance(obj, dict)
        first = from_union([PageLimitPair.from_dict, from_none], obj.get("first"))
        last = from_union([PageLimitPair.from_dict, from_none], obj.get("last"))
        return PaginationLinks(first, last)

    def to_dict(self) -> dict:
        result: dict = {}
        result["first"] = from_union([lambda x: to_class(PageLimitPair, x), from_none], self.first)
        result["last"] = from_union([lambda x: to_class(PageLimitPair, x), from_none], self.last)
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
class Post:
    body: Optional[str] = None
    id: Optional[str] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)
        body = from_union([from_str, from_none], obj.get("body"))
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        return Post(body, id, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["body"] = from_union([from_str, from_none], self.body)
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        return result


@dataclass
class PostsPage:
    data: Optional[List[Optional[Post]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PostsPage':
        assert isinstance(obj, dict)
        data = from_union([lambda x: from_list(lambda x: from_union([Post.from_dict, from_none], x), x), from_none], obj.get("data"))
        return PostsPage(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(Post, x), from_none], x), x), from_none], self.data)
        return result


@dataclass
class User:
    albums: Optional[AlbumsPage] = None
    posts: Optional[PostsPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        albums = from_union([AlbumsPage.from_dict, from_none], obj.get("albums"))
        posts = from_union([PostsPage.from_dict, from_none], obj.get("posts"))
        return User(albums, posts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["albums"] = from_union([lambda x: to_class(AlbumsPage, x), from_none], self.albums)
        result["posts"] = from_union([lambda x: to_class(PostsPage, x), from_none], self.posts)
        return result


@dataclass
class Data:
    update_user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        update_user = from_union([User.from_dict, from_none], obj.get("updateUser"))
        return Data(update_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["updateUser"] = from_union([lambda x: to_class(User, x), from_none], self.update_user)
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
class UpdateUser:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateUser':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return UpdateUser(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def update_user_from_dict(s: Any) -> UpdateUser:
    return UpdateUser.from_dict(s)


def update_user_to_dict(x: UpdateUser) -> Any:
    return to_class(UpdateUser, x)
