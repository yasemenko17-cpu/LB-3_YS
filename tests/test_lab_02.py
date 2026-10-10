"""Автоматична перевірка варіанта 02."""
import pytest
from conftest import load
from kits import lab03

V = load(2)
CASES = [{'id': 'виклик з create',
  'public': True,
  'kind': 'vm',
  'args': ['create'],
  'images': {'db-sys.qcow2': {'format': 'qcow2', 'virtual-size': 32212254720},
             'db-data.qcow2': {'format': 'qcow2', 'virtual-size': 107374182400}},
  'stdout': '',
  'code': 0},
 {'id': 'виклик без аргументів',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': '',
  'code': 3,
  'stderr_contains': 'Використання: vm.sh create'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_02(case):
    lab03.check(V, case)
