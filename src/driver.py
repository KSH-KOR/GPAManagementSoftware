#!/usr/bin/env python
# coding: utf-8

import sys
from HGUCrawler import Crawler
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts

id = sys.argv[1]
pw = sys.argv[2]
c = Crawler()
driver = c.login(id= id, pw= pw)
content = c.getCourseInfo(driver)

client = Client('http://192.168.0.16/wp/xmlrpc.php', 'shinhoo', 'tlsgn5133')
post = WordPressPost()

post.title = 'Course Info'
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

