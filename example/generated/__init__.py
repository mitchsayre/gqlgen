import requests, json
from create_album import CreateAlbum
from create_photo import CreatePhoto
from create_post import CreatePost

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
