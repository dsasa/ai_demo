# import requests

# def post_to_social_media(platform, content, image_url):
#     if platform == "微博":
#         url = "https://api.weibo.com/2/statuses/update.json"
#         data = {"access_token": "YOUR_ACCESS_TOKEN", "status": content, "pic": image_url}
#         response = requests.post(url, data=data)
#         return response.json()
#     elif platform == "推特":
#         url = "https://api.twitter.com/2/tweets"
#         headers = {"Authorization": "Bearer YOUR_BEARER_TOKEN"}
#         data = {"text": content, "media": {"media_ids": [image_url]}}
#         response = requests.post(url, headers=headers, json=data)
#         return response.json()

# post_to_social_media(platform, optimized_response, image_url)