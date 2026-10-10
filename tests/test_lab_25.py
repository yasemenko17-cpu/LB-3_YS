"""Автоматична перевірка варіанта 25."""
import pytest
from conftest import load
from kits import lab03

V = load(25)
CASES = [{'id': 'створення бази даних',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': 'База даних готова\n',
  'code': 0,
  'images': {'db.qcow2': {'format': 'qcow2', 'virtual-size': 53687091200, 'backing': None}}},
 {'id': 'помилка зайві аргументи (1)',
  'public': True,
  'kind': 'vm',
  'args': ['50G'],
  'stdout': '',
  'stderr_contains': 'Без аргументів',
  'code': 1}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_25(case):
    lab03.check(V, case)
