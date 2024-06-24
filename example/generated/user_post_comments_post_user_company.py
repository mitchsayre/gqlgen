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
class Company:
    bs: Optional[str] = None
    catch_phrase: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Company':
        assert isinstance(obj, dict)
        bs = from_union([from_str, from_none], obj.get("bs"))
        catch_phrase = from_union([from_str, from_none], obj.get("catchPhrase"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Company(bs, catch_phrase, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bs"] = from_union([from_str, from_none], self.bs)
        result["catchPhrase"] = from_union([from_str, from_none], self.catch_phrase)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class FluffyUser:
    company: Optional[Company] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyUser':
        assert isinstance(obj, dict)
        company = from_union([Company.from_dict, from_none], obj.get("company"))
        return FluffyUser(company)

    def to_dict(self) -> dict:
        result: dict = {}
        result["company"] = from_union([lambda x: to_class(Company, x), from_none], self.company)
        return result


@dataclass
class PostPost:
    title: Optional[str] = None
    user: Optional[FluffyUser] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PostPost':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        user = from_union([FluffyUser.from_dict, from_none], obj.get("user"))
        return PostPost(title, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["user"] = from_union([lambda x: to_class(FluffyUser, x), from_none], self.user)
        return result


@dataclass
class Comment:
    name: Optional[str] = None
    id: Optional[str] = None
    email: Optional[str] = None
    body: Optional[str] = None
    post: Optional[PostPost] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Comment':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("id"))
        email = from_union([from_str, from_none], obj.get("email"))
        body = from_union([from_str, from_none], obj.get("body"))
        post = from_union([PostPost.from_dict, from_none], obj.get("post"))
        return Comment(name, id, email, body, post)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["id"] = from_union([from_str, from_none], self.id)
        result["email"] = from_union([from_str, from_none], self.email)
        result["body"] = from_union([from_str, from_none], self.body)
        result["post"] = from_union([lambda x: to_class(PostPost, x), from_none], self.post)
        return result


@dataclass
class CommentsPage:
    data: Optional[List[Optional[Comment]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CommentsPage':
        assert isinstance(obj, dict)
        data = from_union([lambda x: from_list(lambda x: from_union([Comment.from_dict, from_none], x), x), from_none], obj.get("data"))
        return CommentsPage(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(Comment, x), from_none], x), x), from_none], self.data)
        return result


@dataclass
class DataPost:
    comments: Optional[CommentsPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataPost':
        assert isinstance(obj, dict)
        comments = from_union([CommentsPage.from_dict, from_none], obj.get("comments"))
        return DataPost(comments)

    def to_dict(self) -> dict:
        result: dict = {}
        result["comments"] = from_union([lambda x: to_class(CommentsPage, x), from_none], self.comments)
        return result


@dataclass
class PostsPage:
    data: Optional[List[Optional[DataPost]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PostsPage':
        assert isinstance(obj, dict)
        data = from_union([lambda x: from_list(lambda x: from_union([DataPost.from_dict, from_none], x), x), from_none], obj.get("data"))
        return PostsPage(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(DataPost, x), from_none], x), x), from_none], self.data)
        return result


@dataclass
class PurpleUser:
    posts: Optional[PostsPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleUser':
        assert isinstance(obj, dict)
        posts = from_union([PostsPage.from_dict, from_none], obj.get("posts"))
        return PurpleUser(posts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["posts"] = from_union([lambda x: to_class(PostsPage, x), from_none], self.posts)
        return result


@dataclass
class Data:
    user: Optional[PurpleUser] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        user = from_union([PurpleUser.from_dict, from_none], obj.get("user"))
        return Data(user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user"] = from_union([lambda x: to_class(PurpleUser, x), from_none], self.user)
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
class UserPostCommentsPostUserCompany:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserPostCommentsPostUserCompany':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return UserPostCommentsPostUserCompany(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def user_post_comments_post_user_company_from_dict(s: Any) -> UserPostCommentsPostUserCompany:
    return UserPostCommentsPostUserCompany.from_dict(s)


def user_post_comments_post_user_company_to_dict(x: UserPostCommentsPostUserCompany) -> Any:
    return to_class(UserPostCommentsPostUserCompany, x)
