"""Автоматична перевірка варіанта 19."""
import pytest
from conftest import load
from kits import lab03

V = load(19)
CASES = [{'id': 'створення образів',
  'public': True,
  'kind': 'vm',
  'args': [],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['test01.qcow2', 'test02.qcow2']},
  'images': {'test01.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240},
             'test02.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240}}},
 {'id': 'конфігурація домену',
  'public': True,
  'kind': 'domain',
  'expect': {'type': 'kvm',
             'name': 'test01',
             'memory_kib': 1048576,
             'vcpus': 1,
             'machine': 'q35',
             'os_type': 'hvm',
             'boot': ['hd'],
             'disks': [{'device': 'disk',
                        'file': '/var/lib/libvirt/images/test01.qcow2',
                        'dev': 'vda',
                        'bus': 'virtio',
                        'fmt': 'qcow2',
                        'readonly': None}],
             'nics': [{'type': 'network', 'network': 'iso-net', 'bridge': None, 'model': 'virtio'}]}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_19(case):
    lab03.check(V, case)
