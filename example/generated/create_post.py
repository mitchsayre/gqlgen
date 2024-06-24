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
class Data:
    create_post: Optional[Post] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        create_post = from_union([Post.from_dict, from_none], obj.get("createPost"))
        return Data(create_post)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createPost"] = from_union([lambda x: to_class(Post, x), from_none], self.create_post)
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
class CreatePost:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreatePost':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return CreatePost(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def create_post_from_dict(s: Any) -> CreatePost:
    return CreatePost.from_dict(s)


def create_post_to_dict(x: CreatePost) -> Any:
    return to_class(CreatePost, x)
