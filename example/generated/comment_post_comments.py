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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class PageLimitPair:
    limit: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PageLimitPair':
        assert isinstance(obj, dict)
        limit = from_union([from_int, from_none], obj.get("limit"))
        return PageLimitPair(limit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["limit"] = from_union([from_int, from_none], self.limit)
        return result


@dataclass
class PaginationLinks:
    prev: Optional[PageLimitPair] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PaginationLinks':
        assert isinstance(obj, dict)
        prev = from_union([PageLimitPair.from_dict, from_none], obj.get("prev"))
        return PaginationLinks(prev)

    def to_dict(self) -> dict:
        result: dict = {}
        result["prev"] = from_union([lambda x: to_class(PageLimitPair, x), from_none], self.prev)
        return result


@dataclass
class PageMetadata:
    total_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PageMetadata':
        assert isinstance(obj, dict)
        total_count = from_union([from_int, from_none], obj.get("totalCount"))
        return PageMetadata(total_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalCount"] = from_union([from_int, from_none], self.total_count)
        return result


@dataclass
class CommentsPage:
    links: Optional[PaginationLinks] = None
    meta: Optional[PageMetadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CommentsPage':
        assert isinstance(obj, dict)
        links = from_union([PaginationLinks.from_dict, from_none], obj.get("links"))
        meta = from_union([PageMetadata.from_dict, from_none], obj.get("meta"))
        return CommentsPage(links, meta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["links"] = from_union([lambda x: to_class(PaginationLinks, x), from_none], self.links)
        result["meta"] = from_union([lambda x: to_class(PageMetadata, x), from_none], self.meta)
        return result


@dataclass
class Post:
    body: Optional[str] = None
    id: Optional[str] = None
    title: Optional[str] = None
    comments: Optional[CommentsPage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)
        body = from_union([from_str, from_none], obj.get("body"))
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        comments = from_union([CommentsPage.from_dict, from_none], obj.get("comments"))
        return Post(body, id, title, comments)

    def to_dict(self) -> dict:
        result: dict = {}
        result["body"] = from_union([from_str, from_none], self.body)
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["comments"] = from_union([lambda x: to_class(CommentsPage, x), from_none], self.comments)
        return result


@dataclass
class Comment:
    body: Optional[str] = None
    email: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    post: Optional[Post] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Comment':
        assert isinstance(obj, dict)
        body = from_union([from_str, from_none], obj.get("body"))
        email = from_union([from_str, from_none], obj.get("email"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        post = from_union([Post.from_dict, from_none], obj.get("post"))
        return Comment(body, email, id, name, post)

    def to_dict(self) -> dict:
        result: dict = {}
        result["body"] = from_union([from_str, from_none], self.body)
        result["email"] = from_union([from_str, from_none], self.email)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["post"] = from_union([lambda x: to_class(Post, x), from_none], self.post)
        return result


@dataclass
class Data:
    comment: Optional[Comment] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        comment = from_union([Comment.from_dict, from_none], obj.get("comment"))
        return Data(comment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["comment"] = from_union([lambda x: to_class(Comment, x), from_none], self.comment)
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
class CommentPostComments:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CommentPostComments':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return CommentPostComments(data, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def comment_post_comments_from_dict(s: Any) -> CommentPostComments:
    return CommentPostComments.from_dict(s)


def comment_post_comments_to_dict(x: CommentPostComments) -> Any:
    return to_class(CommentPostComments, x)
