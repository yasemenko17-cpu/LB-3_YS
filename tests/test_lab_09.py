"""Автоматична перевірка варіанта 09."""
import pytest
from conftest import load
from kits import lab03

V = load(9)
CASES = [{'id': 'успіх qcow2',
  'public': True,
  'kind': 'vm',
  'args': ['stat.qcow2', 'qcow2', '10G'],
  'stdout': 'Створено stat.qcow2 (qcow2)\n',
  'code': 0,
  'images': {'stat.qcow2': {'format': 'qcow2',
                            'virtual-size': 10737418240,
                            'backing': None,
                            'backing-format': None}}},
 {'id': 'неправильний формат',
  'public': True,
  'kind': 'vm',
  'args': ['stat.vmdk', 'vmdk', '10G'],
  'stdout': '',
  'code': 2,
  'stderr_contains': 'Помилка: непідтримуваний формат'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_09(case):
    lab03.check(V, case)
