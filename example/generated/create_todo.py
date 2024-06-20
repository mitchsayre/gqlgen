from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class User:
    phone: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        phone = from_union([from_str, from_none], obj.get("phone"))
        name = from_union([from_str, from_none], obj.get("name"))
        return User(phone, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["phone"] = from_union([from_str, from_none], self.phone)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Todo:
    completed: Optional[bool] = None
    title: Optional[str] = None
    id: Optional[str] = None
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Todo':
        assert isinstance(obj, dict)
        completed = from_union([from_bool, from_none], obj.get("completed"))
        title = from_union([from_str, from_none], obj.get("title"))
        id = from_union([from_str, from_none], obj.get("id"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return Todo(completed, title, id, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["completed"] = from_union([from_bool, from_none], self.completed)
        result["title"] = from_union([from_str, from_none], self.title)
        result["id"] = from_union([from_str, from_none], self.id)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclass
class Data:
    create_todo: Optional[Todo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        create_todo = from_union([Todo.from_dict, from_none], obj.get("createTodo"))
        return Data(create_todo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createTodo"] = from_union([lambda x: to_class(Todo, x), from_none], self.create_todo)
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
class CreateTodo:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreateTodo':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return CreateTodo(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def create_todo_from_dict(s: Any) -> CreateTodo:
    return CreateTodo.from_dict(s)


def create_todo_to_dict(x: CreateTodo) -> Any:
    return to_class(CreateTodo, x)
