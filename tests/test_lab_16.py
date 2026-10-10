"""Автоматична перевірка варіанта 16."""
import pytest
from conftest import load
from kits import lab03

V = load(16)
CASES = [{'id': 'створення образу',
  'public': True,
  'kind': 'vm',
  'args': [],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['web01.qcow2']},
  'images': {'web01.qcow2': {'format': 'qcow2', 'virtual-size': 21474836480}}},
 {'id': 'конфігурація домену',
  'public': True,
  'kind': 'domain',
  'expect': {'type': 'kvm',
             'name': 'web01',
             'memory_kib': 2097152,
             'vcpus': 2,
             'machine': 'q35',
             'os_type': 'hvm',
             'boot': ['hd'],
             'disks': [{'device': 'disk',
                        'file': '/var/lib/libvirt/images/web01.qcow2',
                        'dev': 'vda',
                        'bus': 'virtio',
                        'fmt': 'qcow2',
                        'readonly': None}],
             'nics': [{'type': 'network', 'network': 'web-net', 'bridge': None, 'model': 'virtio'}]}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_16(case):
    lab03.check(V, case)
