import requests

def login(email, password):
    login_url = 'https://www.facebook.com/login/device-based/regular/login/'
    data = {'email': email, 'pass': password}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    session = requests.Session()
    response = session.post(login_url, data=data, headers=headers)
    if 'c_user' in session.cookies.get_dict():
        return session.cookies.get_dict()['c_user']
    else:
        return None

def post_comment(user_id, post_id, comment):
    comment_url = f'https://m.facebook.com/story.php?story_fbid={post_id}'
    data = {'ft_ent_identifier': post_id, 'comment_text': comment}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Cookie': f'c_user={user_id};'
    }
    session = requests.Session()
    response = session.post(comment_url, data=data, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

def main():
    email = input('Enter your Facebook email: ')
    password = input('Enter your Facebook password: ')
    user_id = login(email, password)
    if user_id:
        print("Login successful! User ID:", user_id)
        post_id = input('Enter the ID of the post you want to comment on: ')
        comment_text = input('Enter your comment: ')
        if post_comment(user_id, post_id, comment_text):
            print("Comment posted successfully!")
        else:
            print("Failed to post comment. Please check your post ID.")
    else:
        print("Failed to login. Please check your email and password.")

if __name__ == "__main__":
    main()
