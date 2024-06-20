from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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
    id: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    todos: Optional[TodosPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        todos = from_union([TodosPage.from_dict, from_none], obj.get("todos"))
        return User(id, name, phone, todos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["phone"] = from_union([from_str, from_none], self.phone)
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
class Photo:
    url: Optional[str] = None
    title: Optional[str] = None
    album: Optional[Album] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Photo':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        title = from_union([from_str, from_none], obj.get("title"))
        album = from_union([Album.from_dict, from_none], obj.get("album"))
        return Photo(url, title, album)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_union([from_str, from_none], self.url)
        result["title"] = from_union([from_str, from_none], self.title)
        result["album"] = from_union([lambda x: to_class(Album, x), from_none], self.album)
        return result


@dataclass
class Data:
    create_photo: Optional[Photo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        create_photo = from_union([Photo.from_dict, from_none], obj.get("createPhoto"))
        return Data(create_photo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createPhoto"] = from_union([lambda x: to_class(Photo, x), from_none], self.create_photo)
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
class CreatePhoto:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreatePhoto':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return CreatePhoto(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def create_photo_from_dict(s: Any) -> CreatePhoto:
    return CreatePhoto.from_dict(s)


def create_photo_to_dict(x: CreatePhoto) -> Any:
    return to_class(CreatePhoto, x)
