"""Автоматична перевірка варіанта 17."""
import pytest
from conftest import load
from kits import lab03

V = load(17)
CASES = [{'id': 'створення образів',
  'public': True,
  'kind': 'vm',
  'args': [],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['db01-data.qcow2', 'db01-sys.qcow2']},
  'images': {'db01-sys.qcow2': {'format': 'qcow2', 'virtual-size': 32212254720},
             'db01-data.qcow2': {'format': 'qcow2', 'virtual-size': 107374182400}}},
 {'id': 'конфігурація домену',
  'public': True,
  'kind': 'domain',
  'expect': {'type': 'kvm',
             'name': 'db01',
             'memory_kib': 8388608,
             'vcpus': 4,
             'machine': 'q35',
             'os_type': 'hvm',
             'boot': ['hd'],
             'disks': [{'device': 'disk',
                        'file': '/var/lib/libvirt/images/db01-sys.qcow2',
                        'dev': 'vda',
                        'bus': 'virtio',
                        'fmt': 'qcow2',
                        'readonly': None},
                       {'device': 'disk',
                        'file': '/var/lib/libvirt/images/db01-data.qcow2',
                        'dev': 'vdb',
                        'bus': 'virtio',
                        'fmt': 'qcow2',
                        'readonly': None}],
             'nics': [{'type': 'network', 'network': 'db-net', 'bridge': None, 'model': 'virtio'}]}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_17(case):
    lab03.check(V, case)
