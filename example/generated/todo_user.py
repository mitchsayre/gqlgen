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
    email: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    username: Optional[str] = None
    website: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        email = from_union([from_str, from_none], obj.get("email"))
        name = from_union([from_str, from_none], obj.get("name"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        username = from_union([from_str, from_none], obj.get("username"))
        website = from_union([from_str, from_none], obj.get("website"))
        return User(email, name, phone, username, website)

    def to_dict(self) -> dict:
        result: dict = {}
        result["email"] = from_union([from_str, from_none], self.email)
        result["name"] = from_union([from_str, from_none], self.name)
        result["phone"] = from_union([from_str, from_none], self.phone)
        result["username"] = from_union([from_str, from_none], self.username)
        result["website"] = from_union([from_str, from_none], self.website)
        return result


@dataclass
class Todo:
    completed: Optional[bool] = None
    id: Optional[str] = None
    title: Optional[str] = None
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Todo':
        assert isinstance(obj, dict)
        completed = from_union([from_bool, from_none], obj.get("completed"))
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return Todo(completed, id, title, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["completed"] = from_union([from_bool, from_none], self.completed)
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclass
class Data:
    todo: Optional[Todo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        todo = from_union([Todo.from_dict, from_none], obj.get("todo"))
        return Data(todo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["todo"] = from_union([lambda x: to_class(Todo, x), from_none], self.todo)
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
class TodoUser:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TodoUser':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return TodoUser(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def todo_user_from_dict(s: Any) -> TodoUser:
    return TodoUser.from_dict(s)


def todo_user_to_dict(x: TodoUser) -> Any:
    return to_class(TodoUser, x)
