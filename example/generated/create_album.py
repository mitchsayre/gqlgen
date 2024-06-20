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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


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
class PostsPage:
    links: Optional[PaginationLinks] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PostsPage':
        assert isinstance(obj, dict)
        links = from_union([PaginationLinks.from_dict, from_none], obj.get("links"))
        return PostsPage(links)

    def to_dict(self) -> dict:
        result: dict = {}
        result["links"] = from_union([lambda x: to_class(PaginationLinks, x), from_none], self.links)
        return result


@dataclass
class Todo:
    completed: Optional[bool] = None
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Todo':
        assert isinstance(obj, dict)
        completed = from_union([from_bool, from_none], obj.get("completed"))
        id = from_union([from_str, from_none], obj.get("id"))
        return Todo(completed, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["completed"] = from_union([from_bool, from_none], self.completed)
        result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class TodosPage:
    data: Optional[List[Optional[Todo]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TodosPage':
        assert isinstance(obj, dict)
        data = from_union([lambda x: from_list(lambda x: from_union([Todo.from_dict, from_none], x), x), from_none], obj.get("data"))
        return TodosPage(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(Todo, x), from_none], x), x), from_none], self.data)
        return result


@dataclass
class User:
    name: Optional[str] = None
    email: Optional[str] = None
    posts: Optional[PostsPage] = None
    todos: Optional[TodosPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        email = from_union([from_str, from_none], obj.get("email"))
        posts = from_union([PostsPage.from_dict, from_none], obj.get("posts"))
        todos = from_union([TodosPage.from_dict, from_none], obj.get("todos"))
        return User(name, email, posts, todos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["email"] = from_union([from_str, from_none], self.email)
        result["posts"] = from_union([lambda x: to_class(PostsPage, x), from_none], self.posts)
        result["todos"] = from_union([lambda x: to_class(TodosPage, x), from_none], self.todos)
        return result


@dataclass
class Album:
    id: Optional[str] = None
    title: Optional[str] = None
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Album':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return Album(id, title, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclass
class Data:
    create_album: Optional[Album] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        create_album = from_union([Album.from_dict, from_none], obj.get("createAlbum"))
        return Data(create_album)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createAlbum"] = from_union([lambda x: to_class(Album, x), from_none], self.create_album)
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
class CreateAlbum:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreateAlbum':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return CreateAlbum(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def create_album_from_dict(s: Any) -> CreateAlbum:
    return CreateAlbum.from_dict(s)


def create_album_to_dict(x: CreateAlbum) -> Any:
    return to_class(CreateAlbum, x)
