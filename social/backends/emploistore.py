"""
Emploi Store OAuth2
"""
from social.backends.oauth import BaseOAuth2

class EmploiStoreOAuth2(BaseOAuth2):
    """Emploi Store OAuth authentication backend"""
    name = 'emploi-store'
    ID_KEY = 'sub'
    REDIRECT_STATE = False
    STATE_PARAMETER = False
    AUTHORIZATION_URL = 'https://www.emploi-store.fr/identite/oauth2/authorize'
    ACCESS_TOKEN_URL = 'https://www.emploi-store.fr/identite/oauth2/access_token?realm=/emploistore'
    ACCESS_TOKEN_METHOD = 'POST'
    DEFAULT_SCOPE = ['openid', 'email', 'profile']
    EXTRA_DATA = [
	('refresh_token', 'refresh_token', True),
           ('expires_in', 'expires'),
           ('token_type', 'token_type', True)
    ]

    def auth_extra_arguments(self):
        return {
            'realm': '/emploistore'
        }

    def get_user_details(self, response):
        """Return user details from Emploi Store account"""
        return {'username': response.get('sub'),
                'email': response.get('email') or '',
                'first_name': response.get('given_name'),
                'last_name': response.get('family_name'),
                'fullname': response.get('name')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://www.emploi-store.fr/identite/oauth2/userinfo?realm=/emploistore'
        try:
            return self.get_json(url, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        except ValueError:
            return None
