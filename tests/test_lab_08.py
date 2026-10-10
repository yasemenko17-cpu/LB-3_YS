"""Автоматична перевірка варіанта 08."""
import pytest
from conftest import load
from kits import lab03

V = load(8)
CASES = [{'id': 'успішне створення 20G',
  'public': True,
  'kind': 'vm',
  'args': ['mon.qcow2', '20'],
  'stdout': 'Диск mon.qcow2 розміром 20 G створено\n',
  'code': 0,
  'images': {'mon.qcow2': {'format': 'qcow2',
                           'virtual-size': 21474836480,
                           'backing': None,
                           'backing-format': None}}},
 {'id': 'недостатньо аргументів',
  'public': True,
  'kind': 'vm',
  'args': ['mon.qcow2'],
  'stdout': '',
  'code': 1,
  'stderr_contains': "Використання: vm.sh ІМ'Я РОЗМІР_У_ГБ"}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_08(case):
    lab03.check(V, case)
