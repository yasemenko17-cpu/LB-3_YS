"""Автоматична перевірка варіанта 23."""
import pytest
from conftest import load
from kits import lab03

V = load(23)
CASES = [{'id': 'створення диска моніторингу',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': 'Диск моніторингу створено\n',
  'code': 0,
  'images': {'data.qcow2': {'format': 'qcow2', 'virtual-size': 21474836480, 'backing': None}}},
 {'id': 'помилка зайві аргументи (1)',
  'public': True,
  'kind': 'vm',
  'args': ['10G'],
  'stdout': '',
  'stderr_contains': 'Помилка: аргументи не потрібні',
  'code': 1}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_23(case):
    lab03.check(V, case)
