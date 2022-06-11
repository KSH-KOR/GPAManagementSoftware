#!/usr/bin/env python
# coding: utf-8

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts

class post:
    def post(self, content: str, Title: str):
        client = Client('http://localhost/wp/xmlrpc.php', 'id', 'pw')
        post = WordPressPost()

        post.title = Title
        post.content = content
        post.mime_type = "text/html"

        post.terms_names = {
        'post_tag': ['html5', 'table'],
        'category': ['Introductions', 'HTML5']
        }
        post.post_status = "publish"
        post_id = client.call(posts.NewPost(post))

        print ("Post with id ", post_id, "successfully published")

        # Getting list of posts
        published_posts = client.call(posts.GetPosts({'post_status': 'publish'}))
        print (published_posts)
