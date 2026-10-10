"""Автоматична перевірка варіанта 04."""
import pytest
from conftest import load
from kits import lab03

V = load(4)
CASES = [{'id': 'з аргументом',
  'public': True,
  'kind': 'vm',
  'args': ['iso-sys.qcow2'],
  'images': {'iso-sys.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240}},
  'stdout': '',
  'code': 0},
 {'id': 'без аргументів',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': '',
  'code': 4,
  'stderr_contains': 'Використання: vm.sh <назва_файлу>'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_04(case):
    lab03.check(V, case)
