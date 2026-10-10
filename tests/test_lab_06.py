"""Автоматична перевірка варіанта 06."""
import pytest
from conftest import load
from kits import lab03

V = load(6)
CASES = [{'id': 'успішне створення 15G',
  'public': True,
  'kind': 'vm',
  'args': ['disk1.qcow2', '15G'],
  'stdout': 'Створено диск disk1.qcow2\n',
  'code': 0,
  'images': {'disk1.qcow2': {'format': 'qcow2',
                             'virtual-size': 16106127360,
                             'backing': None,
                             'backing-format': None}}},
 {'id': 'недостатньо аргументів',
  'public': True,
  'kind': 'vm',
  'args': ['disk1.qcow2'],
  'stdout': '',
  'code': 1,
  'stderr_contains': "Використання: vm.sh ІМ'Я РОЗМІР"}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_06(case):
    lab03.check(V, case)
