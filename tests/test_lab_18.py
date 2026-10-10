"""Автоматична перевірка варіанта 18."""
import pytest
from conftest import load
from kits import lab03

V = load(18)
CASES = [{'id': 'створення оверлею',
  'public': True,
  'kind': 'vm',
  'args': [],
  'files': {'base.qcow2': {'text': 'dummy'}},
  'env': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['base.qcow2', 'dev01.qcow2']},
  'images': {'dev01.qcow2': {'format': 'qcow2',
                             'virtual-size': 53687091200,
                             'backing': 'base.qcow2',
                             'backing-format': 'qcow2'}}},
 {'id': 'конфігурація домену',
  'public': True,
  'kind': 'domain',
  'expect': {'type': 'kvm',
             'name': 'dev01',
             'memory_kib': 4194304,
             'vcpus': 2,
             'machine': 'q35',
             'os_type': 'hvm',
             'boot': ['hd'],
             'disks': [{'device': 'disk',
                        'file': '/var/lib/libvirt/images/dev01.qcow2',
                        'dev': 'vda',
                        'bus': 'virtio',
                        'fmt': 'qcow2',
                        'readonly': None}],
             'nics': [{'type': 'network', 'network': 'dev-net', 'bridge': None, 'model': 'virtio'}]}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_18(case):
    lab03.check(V, case)
