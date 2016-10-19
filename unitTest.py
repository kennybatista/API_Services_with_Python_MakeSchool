import API_Services_Code_Challenges as server
import unittest

class FlaskServerTest(unittest.TestCase):

    def setUp(self):
        # Run app in testing mode to retrieve exceptions and stack traces
        server.app.testing = True
        self.app = server.app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        assert response.status_code == 200, "status_code was not OK"
        print response

    if __name__ == '__main':
        unittest.main()
