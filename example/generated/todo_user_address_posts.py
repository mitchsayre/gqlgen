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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class Address:
    city: Optional[str] = None
    street: Optional[str] = None
    suite: Optional[str] = None
    zipcode: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        assert isinstance(obj, dict)
        city = from_union([from_str, from_none], obj.get("city"))
        street = from_union([from_str, from_none], obj.get("street"))
        suite = from_union([from_str, from_none], obj.get("suite"))
        zipcode = from_union([from_str, from_none], obj.get("zipcode"))
        return Address(city, street, suite, zipcode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["city"] = from_union([from_str, from_none], self.city)
        result["street"] = from_union([from_str, from_none], self.street)
        result["suite"] = from_union([from_str, from_none], self.suite)
        result["zipcode"] = from_union([from_str, from_none], self.zipcode)
        return result


@dataclass
class Post:
    body: Optional[str] = None
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)
        body = from_union([from_str, from_none], obj.get("body"))
        id = from_union([from_str, from_none], obj.get("id"))
        return Post(body, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["body"] = from_union([from_str, from_none], self.body)
        result["id"] = from_union([from_str, from_none], self.id)
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
    address: Optional[Address] = None
    email: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    posts: Optional[PostsPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        address = from_union([Address.from_dict, from_none], obj.get("address"))
        email = from_union([from_str, from_none], obj.get("email"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        posts = from_union([PostsPage.from_dict, from_none], obj.get("posts"))
        return User(address, email, id, name, posts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_union([lambda x: to_class(Address, x), from_none], self.address)
        result["email"] = from_union([from_str, from_none], self.email)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["posts"] = from_union([lambda x: to_class(PostsPage, x), from_none], self.posts)
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
class TodoUserAddressPosts:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TodoUserAddressPosts':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return TodoUserAddressPosts(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def todo_user_address_posts_from_dict(s: Any) -> TodoUserAddressPosts:
    return TodoUserAddressPosts.from_dict(s)


def todo_user_address_posts_to_dict(x: TodoUserAddressPosts) -> Any:
    return to_class(TodoUserAddressPosts, x)
