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
    username: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        email = from_union([from_str, from_none], obj.get("email"))
        name = from_union([from_str, from_none], obj.get("name"))
        username = from_union([from_str, from_none], obj.get("username"))
        return User(email, name, username)

    def to_dict(self) -> dict:
        result: dict = {}
        result["email"] = from_union([from_str, from_none], self.email)
        result["name"] = from_union([from_str, from_none], self.name)
        result["username"] = from_union([from_str, from_none], self.username)
        return result


@dataclass
class Data:
    create_user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        create_user = from_union([User.from_dict, from_none], obj.get("createUser"))
        return Data(create_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createUser"] = from_union([lambda x: to_class(User, x), from_none], self.create_user)
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
class CreateUser:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreateUser':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return CreateUser(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def create_user_from_dict(s: Any) -> CreateUser:
    return CreateUser.from_dict(s)


def create_user_to_dict(x: CreateUser) -> Any:
    return to_class(CreateUser, x)
