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
class Data:
    delete_user: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        delete_user = from_union([from_bool, from_none], obj.get("deleteUser"))
        return Data(delete_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["deleteUser"] = from_union([from_bool, from_none], self.delete_user)
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
class DeleteUser:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeleteUser':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return DeleteUser(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def delete_user_from_dict(s: Any) -> DeleteUser:
    return DeleteUser.from_dict(s)


def delete_user_to_dict(x: DeleteUser) -> Any:
    return to_class(DeleteUser, x)
