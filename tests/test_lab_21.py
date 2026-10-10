"""Автоматична перевірка варіанта 21."""
import pytest
from conftest import load
from kits import lab03

V = load(21)
CASES = [{'id': 'створення диска 10G',
  'public': True,
  'kind': 'vm',
  'args': ['system.qcow2', '10G'],
  'stdout': 'Створено: system.qcow2 10G\n',
  'code': 0,
  'images': {'system.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240, 'backing': None}}},
 {'id': 'помилка аргументів (0)',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': '',
  'stderr_contains': 'Використання: vm.sh ФАЙЛ РОЗМІР',
  'code': 1}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_21(case):
    lab03.check(V, case)
