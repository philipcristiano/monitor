from mock import patch, MagicMock

from monitor.monitors.load import monitor_load

class TestLoad(object):

    def setup(self):
        self.record = MagicMock()
        self.open_mock = MagicMock()
        self.loadavg = '1.44 1.39 0.72 1/151 1565'
        self.line = self.open_mock.return_value.readall.return_value = self.loadavg

        with patch('__builtin__.open', self.open_mock) as open_mock:
            monitor_load(self.record)

    def test_records_1min(self):
        self.record.assert_any_call('1_min', 1.4399999999999999)

    def test_records_5min(self):
        self.record.assert_any_call('5_min', 1.3899999999999999)

    def test_records_15min(self):
        self.record.assert_any_call('15_min', 0.71999999999999997)

    def test_records_runnable_tasks(self):
        self.record.assert_any_call('runnable_tasks', 1.0)

    def test_records_total_tasks(self):
        self.record.assert_any_call('total_tasks', 151.0)

    def test_records_last_pid(self):
        self.record.assert_any_call('last_pid', 1565.0)
