from accounts.models import ListUser
import requests
from django.contrib.auth import get_user_model

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'
DOMAIN = 'localhost'
User = get_user_model()


class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(
            PERSONA_VERIFY_URL,
            data={'assertion': assertion, 'audience': DOMAIN}
        )

        if not response.ok:
            return

        if response.json()['status'] == 'okay':
            email = response.json()['email']

            try:
                return self.get_user(email)
            except User.DoesNotExist:
                return User.objects.create(email=email)

            return self.get_user(email)

    def get_user(self, email):
        return User.objects.get(email=email)


class PersonaAuthenticationBackend2(object):

    def authenticate(self, assertion):
        data = {'assertion': assertion, 'audience': 'localhost'}

        # print 'sending to mozilla', data

        resp = requests.post(
            'https://verifier.login.persona.org/verify', data=data)

        # print 'got response: ', resp

        if resp.ok:
            verification_data = resp.json()

            if verification_data['status'] == 'okay':
                email = verification_data['email']

                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.objects.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)
