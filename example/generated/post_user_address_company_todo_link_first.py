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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Address:
    city: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        assert isinstance(obj, dict)
        city = from_union([from_str, from_none], obj.get("city"))
        return Address(city)

    def to_dict(self) -> dict:
        result: dict = {}
        result["city"] = from_union([from_str, from_none], self.city)
        return result


@dataclass
class Company:
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Company':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        return Company(name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        return result


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
class TodosPage:
    links: Optional[PaginationLinks] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TodosPage':
        assert isinstance(obj, dict)
        links = from_union([PaginationLinks.from_dict, from_none], obj.get("links"))
        return TodosPage(links)

    def to_dict(self) -> dict:
        result: dict = {}
        result["links"] = from_union([lambda x: to_class(PaginationLinks, x), from_none], self.links)
        return result


@dataclass
class User:
    address: Optional[Address] = None
    company: Optional[Company] = None
    todos: Optional[TodosPage] = None
    username: Optional[str] = None
    website: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        address = from_union([Address.from_dict, from_none], obj.get("address"))
        company = from_union([Company.from_dict, from_none], obj.get("company"))
        todos = from_union([TodosPage.from_dict, from_none], obj.get("todos"))
        username = from_union([from_str, from_none], obj.get("username"))
        website = from_union([from_str, from_none], obj.get("website"))
        return User(address, company, todos, username, website)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_union([lambda x: to_class(Address, x), from_none], self.address)
        result["company"] = from_union([lambda x: to_class(Company, x), from_none], self.company)
        result["todos"] = from_union([lambda x: to_class(TodosPage, x), from_none], self.todos)
        result["username"] = from_union([from_str, from_none], self.username)
        result["website"] = from_union([from_str, from_none], self.website)
        return result


@dataclass
class Post:
    id: Optional[str] = None
    title: Optional[str] = None
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return Post(id, title, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclass
class Data:
    post: Optional[Post] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        post = from_union([Post.from_dict, from_none], obj.get("post"))
        return Data(post)

    def to_dict(self) -> dict:
        result: dict = {}
        result["post"] = from_union([lambda x: to_class(Post, x), from_none], self.post)
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
class PostUserAddressCompanyTodoLinkFirst:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PostUserAddressCompanyTodoLinkFirst':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return PostUserAddressCompanyTodoLinkFirst(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def post_user_address_company_todo_link_first_from_dict(s: Any) -> PostUserAddressCompanyTodoLinkFirst:
    return PostUserAddressCompanyTodoLinkFirst.from_dict(s)


def post_user_address_company_todo_link_first_to_dict(x: PostUserAddressCompanyTodoLinkFirst) -> Any:
    return to_class(PostUserAddressCompanyTodoLinkFirst, x)
