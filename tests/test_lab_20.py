"""Автоматична перевірка варіанта 20."""
import pytest
from conftest import load
from kits import lab03

V = load(20)
CASES = [{'id': 'створення образу',
  'public': True,
  'kind': 'vm',
  'args': [],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['gw01.qcow2']},
  'images': {'gw01.qcow2': {'format': 'qcow2', 'virtual-size': 16106127360}}},
 {'id': 'помилка аргументів',
  'public': True,
  'kind': 'vm',
  'args': ['arg'],
  'stdout': '',
  'code': 1,
  'stderr_contains': 'Помилка: аргументи не допускаються'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_20(case):
    lab03.check(V, case)
