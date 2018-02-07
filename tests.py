from requests import post

### VERY MUCH A WORK IN PROGRESS

launch = {
  "version": "1.0",
  "session": {
    "new": True,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "LaunchRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
    "intent": {
      "name": "TestPlay",
      "slots": {
        }
      }
    }
}


def _post(route='/', data={}):
    url = 'http://127.0.0.1:5000' + str(route)
    print('POSTing to %s' % url)
    response = post(url, json=data)
    self.assertEqual(200, response.status_code)
    return response

def test_helloworld():
    """ Test the HelloWorld sample project """

    response = self._post(data=launch)
    self.assertTrue('hello' in self._get_text(response))