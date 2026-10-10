"""Автоматична перевірка варіанта 13."""
import pytest
from conftest import load
from kits import lab03

V = load(13)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['15G', '100G'],
  'stdout': 'Створено fs-sys: 15G, fs-data: 100G\n',
  'code': 0,
  'images': {'fs-sys.qcow2': {'format': 'qcow2', 'virtual-size': 16106127360},
             'fs-data.qcow2': {'format': 'qcow2', 'virtual-size': 107374182400}}},
 {'id': 'бракує аргументів',
  'public': True,
  'kind': 'vm',
  'args': ['15G'],
  'stdout': '',
  'code': 1,
  'stderr_contains': 'Використання: vm.sh РОЗМІР_ОС РОЗМІР_ДАНИХ'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_13(case):
    lab03.check(V, case)
