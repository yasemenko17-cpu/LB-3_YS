"""Автоматична перевірка варіанта 14."""
import pytest
from conftest import load
from kits import lab03

V = load(14)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['5G'],
  'stdout': 'Створено диск шлюзу розміром 5G\n',
  'code': 0,
  'images': {'gw-sys.qcow2': {'format': 'qcow2', 'virtual-size': 5368709120}}},
 {'id': 'бракує аргументів',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': '',
  'code': 1,
  'stderr_contains': 'Використання: vm.sh РОЗМІР'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_14(case):
    lab03.check(V, case)
