"""Автоматична перевірка варіанта 05."""
import pytest
from conftest import load
from kits import lab03

V = load(5)
CASES = [{'id': 'з -s',
  'public': True,
  'kind': 'vm',
  'args': ['-s', '40'],
  'images': {'gate-sys.qcow2': {'format': 'qcow2', 'virtual-size': 42949672960}},
  'stdout': '',
  'code': 0},
 {'id': 'без аргументів',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': '',
  'code': 5,
  'stderr_contains': 'Використання: vm.sh -s РОЗМІР'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_05(case):
    lab03.check(V, case)
