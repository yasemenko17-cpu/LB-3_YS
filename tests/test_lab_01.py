"""Автоматична перевірка варіанта 01."""
import pytest
from conftest import load
from kits import lab03

V = load(1)
CASES = [{'id': 'без аргументів успіх',
  'public': True,
  'kind': 'vm',
  'args': [],
  'images': {'web-sys.qcow2': {'format': 'qcow2', 'virtual-size': 21474836480}},
  'stdout': '',
  'code': 0},
 {'id': 'з аргументами помилка',
  'public': True,
  'kind': 'vm',
  'args': ['--test'],
  'stdout': '',
  'code': 2,
  'stderr_contains': 'Помилка: аргументи не потрібні'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_01(case):
    lab03.check(V, case)
