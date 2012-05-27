from mock import patch, MagicMock
from nose.tools import eq_

from monitor.monitors.memory import monitor_memory
import monitor.monitors.memory as mod


@patch.object(mod, 'read_file')
def test_memory(mock_read_file):
    mock_read_file.return_value = MEMINFO.split('\n')
    mock_record = MagicMock(name='record')
    monitor_memory(mock_record)

    mock_record.assert_any_call('MemFree', '69936')


MEMINFO = """MemTotal:       255908 kB
MemFree:         69936 kB
Buffers:         15812 kB
Cached:         115124 kB
SwapCached:          0 kB
Active:          92700 kB
Inactive:        63792 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:       255908 kB
LowFree:         69936 kB
SwapTotal:      524280 kB
SwapFree:       524280 kB
Dirty:               4 kB
Writeback:           0 kB
Mapped:          42236 kB
Slab:            25912 kB
Committed_AS:   118680 kB
PageTables:       1236 kB
VmallocTotal:  3874808 kB
VmallocUsed:      1416 kB
VmallocChunk:  3872908 kB
HugePages_Total:     0
HugePages_Free:      0
Hugepagesize:     4096 kB"""
