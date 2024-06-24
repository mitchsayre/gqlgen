import requests, json
from create_album import CreateAlbum
from create_photo import CreatePhoto
from create_post import CreatePost
from create_todo import CreateTodo
from create_user import CreateUser
from delete_album import DeleteAlbum
from delete_user import DeleteUser
from update_comment import UpdateComment
from update_photo import UpdatePhoto
from update_post import UpdatePost
from update_todo import updateTodo
from update_user import UpdateUser
from album_user_posts import AlbumUserPosts
from albums_link_meta import AlbumsLinkMeta
from comment_post_comments import CommentPostComments
from comments import Comments
from photo_album_photos_meta import PhotoAlbumPhotosMeta
from photos import Photos
from post_meta_comments import PostMetaComments
from post_user_address_company_todo_link_first import PostUserAddressCompanyTodoLinkFirst
from todo_user import TodoUser
from todo_user_address_posts import TodoUserAddressPosts
from user import User
from user_meta import UserMeta
from user_post_comments_post_user_company import UserPostCommentsPostUserCompany

class GqlgenClient:
  def __init__(self, config):
    self.config = config

  def execute_operation(self, input, operation_name, document):
    url = self.config.url
    headers = self.config.headers
    body = {
        "query": document,
        "operationName": operation_name,
        "variables": input,
    }

    res = requests.post(url, headers=headers, data=json.dumps(body))
    return res.json()
  
  def create_album(self, input) -> CreateAlbum:
    res = self.execute_operation(
      self,
      input,
      "CreateAlbum",
      'mutation CreateAlbum($input: CreateAlbumInput!) {   createAlbum(input: $input) {     id     title     user {       name       email       posts {         links {           first {             limit             page           }           last {             limit             page           }         }       }       todos {         data {           completed           id         }       }     }   } }'
    )
    return CreateAlbum.from_dict(res)

  def create_photo(self, input) -> CreatePhoto:
    res = self.execute_operation(
      self,
      input,
      "CreatePhoto",
      'mutation CreatePhoto($input: CreatePhotoInput!) {   createPhoto(input: $input) {     url     title     album {       id       title       user {         id         name         phone         todos {           data {             completed             id           }         }       }     }   } }'
    )
    return CreatePhoto.from_dict(res)

  def create_post(self, input) -> CreatePost:
    res = self.execute_operation(
      self,
      input,
      "CreatePost",
      'mutation CreatePost($input: CreatePostInput!) {   createPost(input: $input) {     body     id     title   } }'
    )
    return CreatePost.from_dict(res)

  def create_todo(self, input) -> CreateTodo:
    res = self.execute_operation(
      self,
      input,
      "CreateTodo",
      'mutation CreateTodo($input: CreateTodoInput!) {   createTodo(input: $input) {     completed     title     id     user {       phone       name     }   } }'
    )
    return CreateTodo.from_dict(res)

  def create_user(self, input) -> CreateUser:
    res = self.execute_operation(
      self,
      input,
      "CreateUser",
      'mutation CreateUser($input: CreateUserInput!) {   createUser(input: $input) {     email     name     username   } }'
    )
    return CreateUser.from_dict(res)

  def delete_album(self, input) -> DeleteAlbum:
    res = self.execute_operation(
      self,
      input,
      "DeleteAlbum",
      'mutation DeleteAlbum {   deleteAlbum(id: "123") }'
    )
    return DeleteAlbum.from_dict(res)

  def delete_user(self, input) -> DeleteUser:
    res = self.execute_operation(
      self,
      input,
      "DeleteUser",
      'mutation DeleteUser($deleteUserId: ID!) {   deleteUser(id: $deleteUserId) }'
    )
    return DeleteUser.from_dict(res)

  def update_comment(self, input) -> UpdateComment:
    res = self.execute_operation(
      self,
      input,
      "UpdateComment",
      'mutation UpdateComment($updateCommentId: ID!, $input: UpdateCommentInput!) {   updateComment(id: $updateCommentId, input: $input) {     body     email     id     name   } }'
    )
    return UpdateComment.from_dict(res)

  def update_photo(self, input) -> UpdatePhoto:
    res = self.execute_operation(
      self,
      input,
      "UpdatePhoto",
      'mutation UpdatePhoto($updatePhotoId: ID!, $input: UpdatePhotoInput!) {   updatePhoto(id: $updatePhotoId, input: $input) {     album {       id       title     }     id     title     url   } }'
    )
    return UpdatePhoto.from_dict(res)

  def update_post(self, input) -> UpdatePost:
    res = self.execute_operation(
      self,
      input,
      "UpdatePost",
      'mutation UpdatePost($updatePostId: ID!, $input: UpdatePostInput!) {   updatePost(id: $updatePostId, input: $input) {     body     id     comments {       links {         first {           limit           page         }       }       meta {         totalCount       }     }   } }'
    )
    return UpdatePost.from_dict(res)

  def update_todo(self, input) -> updateTodo:
    res = self.execute_operation(
      self,
      input,
      "updateTodo",
      'mutation updateTodo($updateTodoId: ID!, $input: UpdateTodoInput!) {   updateTodo(id: $updateTodoId, input: $input) {     completed     id     title   } }'
    )
    return updateTodo.from_dict(res)

  def update_user(self, input) -> UpdateUser:
    res = self.execute_operation(
      self,
      input,
      "UpdateUser",
      'mutation UpdateUser($updateUserId: ID!, $input: UpdateUserInput!) {   updateUser(id: $updateUserId, input: $input) {     albums {       links {         first {           limit           page         }         last {           limit           page         }       }       meta {         totalCount       }     }     posts {       data {         body         id         title       }     }   } }'
    )
    return UpdateUser.from_dict(res)

  def album_user_posts(self, input) -> AlbumUserPosts:
    res = self.execute_operation(
      self,
      input,
      "AlbumUserPosts",
      'query AlbumUserPosts($options: PageQueryOptions) {   album(id: "10") {     id     title     user {       id       email       name       posts(options: $options) {         data {           title           id         }       }     }   } }'
    )
    return AlbumUserPosts.from_dict(res)

  def albums_link_meta(self, input) -> AlbumsLinkMeta:
    res = self.execute_operation(
      self,
      input,
      "AlbumsLinkMeta",
      'query AlbumsLinkMeta($options: PageQueryOptions) {   albums(options: $options) {     links {       first {         limit         page       }     }     meta {       totalCount     }   } }'
    )
    return AlbumsLinkMeta.from_dict(res)

  def comment_post_comments(self, input) -> CommentPostComments:
    res = self.execute_operation(
      self,
      input,
      "CommentPostComments",
      'query CommentPostComments($commentId: ID!, $options: PageQueryOptions) {   comment(id: $commentId) {     body     email     id     name     post {       body       id       title       comments(options: $options) {         links {           prev {             limit           }         }         meta {           totalCount         }       }     }   } }'
    )
    return CommentPostComments.from_dict(res)

  def comments(self, input) -> Comments:
    res = self.execute_operation(
      self,
      input,
      "Comments",
      'query Comments {   comment(id: "45") {     body     email     id     name   } }'
    )
    return Comments.from_dict(res)

  def photo_album_photos_meta(self, input) -> PhotoAlbumPhotosMeta:
    res = self.execute_operation(
      self,
      input,
      "PhotoAlbumPhotosMeta",
      'query PhotoAlbumPhotosMeta($photoId: ID!) {   photo(id: $photoId) {     id     thumbnailUrl     title     url     album {       title       id       photos {         meta {           totalCount         }         data {           thumbnailUrl         }       }     }   } }'
    )
    return PhotoAlbumPhotosMeta.from_dict(res)

  def photos(self, input) -> Photos:
    res = self.execute_operation(
      self,
      input,
      "Photos",
      'query Photos($options: PageQueryOptions) {   photos(options: $options) {     data {       id       title     }   } }'
    )
    return Photos.from_dict(res)

  def post_meta_comments(self, input) -> PostMetaComments:
    res = self.execute_operation(
      self,
      input,
      "PostMetaComments",
      'query PostMetaComments($options: PageQueryOptions) {   posts {     meta {       totalCount     }     data {       body       id       comments(options: $options) {         links {           first {             page           }         }       }     }   } }'
    )
    return PostMetaComments.from_dict(res)

  def post_user_address_company_todo_link_first(self, input) -> PostUserAddressCompanyTodoLinkFirst:
    res = self.execute_operation(
      self,
      input,
      "PostUserAddressCompanyTodoLinkFirst",
      'query PostUserAddressCompanyTodoLinkFirst {   post(id: "234") {     id     title     user {       address {         city       }       company {         name       }       todos {         links {           first {             limit             page           }         }       }       username       website     }   } }'
    )
    return PostUserAddressCompanyTodoLinkFirst.from_dict(res)

  def todo_user(self, input) -> TodoUser:
    res = self.execute_operation(
      self,
      input,
      "TodoUser",
      'query TodoUser($todoId: ID!) {   todo(id: $todoId) {     completed     id     title     user {       email       name       phone       username       website     }   } }'
    )
    return TodoUser.from_dict(res)

  def todo_user_address_posts(self, input) -> TodoUserAddressPosts:
    res = self.execute_operation(
      self,
      input,
      "TodoUserAddressPosts",
      'query TodoUserAddressPosts($todoId: ID!, $options: PageQueryOptions) {   todo(id: $todoId) {     completed     id     title     user {       address {         city         street         suite         zipcode       }       email       id       name       posts(options: $options) {         data {           body           id         }       }     }   } }'
    )
    return TodoUserAddressPosts.from_dict(res)

  def user(self, input) -> User:
    res = self.execute_operation(
      self,
      input,
      "User",
      'query User {   user(id: "1") {     id     email     name   } }'
    )
    return User.from_dict(res)

  def user_meta(self, input) -> UserMeta:
    res = self.execute_operation(
      self,
      input,
      "UserMeta",
      'query UserMeta($options: PageQueryOptions) {   users(options: $options) {     meta {       totalCount     }   } }'
    )
    return UserMeta.from_dict(res)

  def user_post_comments_post_user_company(self, input) -> UserPostCommentsPostUserCompany:
    res = self.execute_operation(
      self,
      input,
      "UserPostCommentsPostUserCompany",
      'query UserPostCommentsPostUserCompany($userId: ID!) {   user(id: $userId) {     posts {       data {         comments {           data {             name             id             email             body             post {               title               user {                 company {                   bs                   catchPhrase                   name                 }               }             }           }         }       }     }   } }'
    )
    return UserPostCommentsPostUserCompany.from_dict(res)