import requests, json
from album_user_posts import AlbumUserPosts


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

    def album_user_posts(self, input) -> AlbumUserPosts:
        res = self.execute_operation(
            self,
            input,
            "AlbumUserPosts",
            'query AlbumUserPosts($options: PageQueryOptions) { album(id: "10") { id title user { id email name posts(options: $options) { data { title id } } } } }',
        )
        return AlbumUserPosts.to_dict(res)

    # TODO: Implement entrypointPlugin.ts to generate the operation functions like album_user_posts
