"""Автоматична перевірка варіанта 22."""
import pytest
from conftest import load
from kits import lab03

V = load(22)
CASES = [{'id': 'створення кластера 10G',
  'public': True,
  'kind': 'vm',
  'args': ['10G'],
  'stdout': 'Кластер на 10G створено\n',
  'code': 0,
  'images': {'base.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240, 'backing': None},
             'node1.qcow2': {'format': 'qcow2',
                             'virtual-size': 10737418240,
                             'backing': 'base.qcow2',
                             'backing-format': 'qcow2'},
             'node2.qcow2': {'format': 'qcow2',
                             'virtual-size': 10737418240,
                             'backing': 'base.qcow2',
                             'backing-format': 'qcow2'},
             'node3.qcow2': {'format': 'qcow2',
                             'virtual-size': 10737418240,
                             'backing': 'base.qcow2',
                             'backing-format': 'qcow2'}}},
 {'id': 'помилка аргументів (0)',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': '',
  'stderr_contains': 'Використання: vm.sh РОЗМІР',
  'code': 1}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_22(case):
    lab03.check(V, case)
