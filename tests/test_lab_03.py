"""Автоматична перевірка варіанта 03."""
import pytest
from conftest import load
from kits import lab03

V = load(3)
CASES = [{'id': 'створення образів успіх',
  'public': True,
  'kind': 'vm',
  'args': [],
  'images': {'base-ubuntu.qcow2': {'format': 'qcow2', 'virtual-size': 16106127360},
             'dev-overlay.qcow2': {'format': 'qcow2',
                                   'backing': 'base-ubuntu.qcow2',
                                   'backing-format': 'qcow2',
                                   'virtual-size': 16106127360}},
  'stdout': '',
  'code': 0},
 {'id': 'з аргументами помилка',
  'public': True,
  'kind': 'vm',
  'args': ['arg'],
  'stdout': '',
  'code': 1,
  'stderr_contains': 'Помилка: аргументи не допускаються'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_03(case):
    lab03.check(V, case)
