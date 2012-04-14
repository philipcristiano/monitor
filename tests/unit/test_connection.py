from mock import patch, MagicMock
from nose.tools import eq_

from monitor.connection import create_connection


class TestConnection(object):

    def setup(self):
        self.puka = MagicMock()
        self.client = self.puka.Client.return_value

        with patch('monitor.connection.puka', self.puka) as puka_mock:
            self.returned = create_connection()

    def test_creates_client(self):
        self.puka.Client.assert_any_call('amqp://33.33.33.10/')

    def test_client_waits_for_connect_promise(self):
        self.client.wait.assert_any_call(self.client.connect.return_value)

    def  test_returns_client(self):
        eq_(self.returned, self.client)


