from mock import patch, MagicMock

from monitor.monitors.load import monitor_load

class TestLoad(object):

    def setup(self):
        self.record = MagicMock()
        self.open_mock = MagicMock()

    def test_records_load(self):
        with patch('__builtin__.open', self.open_mock) as open_mock:
            monitor_load(self.record)
        self.open_mock.assert_called_with('/proc/loadavg')
