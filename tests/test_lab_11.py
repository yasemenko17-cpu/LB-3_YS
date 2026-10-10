"""Автоматична перевірка варіанта 11."""
import pytest
from conftest import load
from kits import lab03

V = load(11)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['10G', '50G'],
  'stdout': 'Створено диски: ОС 10G, Дані 50G\n',
  'code': 0,
  'images': {'system.raw': {'format': 'raw', 'virtual-size': 10737418240},
             'data.qcow2': {'format': 'qcow2', 'virtual-size': 53687091200}}},
 {'id': 'бракує аргументів',
  'public': True,
  'kind': 'vm',
  'args': ['10G'],
  'stdout': '',
  'code': 1,
  'stderr_contains': 'Використання: vm.sh РОЗМІР_ОС РОЗМІР_ДАНИХ'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_11(case):
    lab03.check(V, case)
