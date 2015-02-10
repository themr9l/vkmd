from app import app
from flask import redirect, request
from urllib.parse import urlunparse, urlencode


@app.route('/get_token')
def get_token():

    payload = {
        'client_id': '4454433',
        'scope': 'audio',
        'redirect_uri': request.url_root + 'get_token_redirect',
        'display': 'page',
        'v': '5.28',
        'response_type': 'token',
    }
    params_str = urlencode(payload)
    auth_url = urlunparse(
        ('https', 'oauth.vk.com', 'authorize', '', params_str, ''))

    print(auth_url)

    return redirect(auth_url)

@app.route('/get_token_redirect')
def get_token_redirect():
    return ''
