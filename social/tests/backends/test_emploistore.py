import json

from social.tests.backends.oauth import OAuth2Test


class EmploiStoreOAuth2Test(OAuth2Test):
    backend_path = 'social.backends.emploistore.EmploiStoreOAuth2'
    user_data_url = 'https://www.emploi-store.fr/identite/oauth2/userinfo?realm=/emploistore'
    expected_username = 'FooBar'
    access_token_body = json.dumps({
        'access_token': 'foobar',
        'token_type': 'bearer'
    })
    user_data_body = json.dumps({
        'sub': 'FooBar',
        'email': 'foo@bar.com',
        'given_name': 'Foo Bar'
    })

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()
