from instapy_cli import client

username = ""
password = ""
image = "images/suntree.png"
caption = "this is an auto-generated post"

with client(username, password) as cli:
    cli.upload(image, caption)
