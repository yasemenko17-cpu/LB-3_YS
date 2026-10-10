"""Автоматична перевірка варіанта 24."""
import pytest
from conftest import load
from kits import lab03

V = load(24)
CASES = [{'id': 'створення raw-диска 5G',
  'public': True,
  'kind': 'vm',
  'args': ['5G'],
  'stdout': 'RAW-диск gw.raw на 5G створено\n',
  'code': 0,
  'images': {'gw.raw': {'format': 'raw', 'virtual-size': 5368709120, 'backing': None}}},
 {'id': 'помилка аргументів (0)',
  'public': True,
  'kind': 'vm',
  'args': [],
  'stdout': '',
  'stderr_contains': 'Використання: vm.sh РОЗМІР',
  'code': 1}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_24(case):
    lab03.check(V, case)
