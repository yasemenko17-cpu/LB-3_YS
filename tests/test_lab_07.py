"""Автоматична перевірка варіанта 07."""
import pytest
from conftest import load
from kits import lab03

V = load(7)
CASES = [{'id': 'успішне створення перекриттів',
  'public': True,
  'kind': 'vm',
  'args': ['base.qcow2', 'n1.qcow2', 'n2.qcow2', 'n3.qcow2'],
  'files': {'base.qcow2': ''},
  'stdout': 'Створено перекриття: n1.qcow2, n2.qcow2, n3.qcow2\n',
  'code': 0,
  'images': {'n1.qcow2': {'format': 'qcow2',
                          'virtual-size': 10737418240,
                          'backing': 'base.qcow2',
                          'backing-format': 'qcow2'},
             'n2.qcow2': {'format': 'qcow2',
                          'virtual-size': 10737418240,
                          'backing': 'base.qcow2',
                          'backing-format': 'qcow2'},
             'n3.qcow2': {'format': 'qcow2',
                          'virtual-size': 10737418240,
                          'backing': 'base.qcow2',
                          'backing-format': 'qcow2'}}},
 {'id': 'недостатньо аргументів',
  'public': True,
  'kind': 'vm',
  'args': ['base.qcow2', 'n1.qcow2'],
  'stdout': '',
  'code': 1,
  'stderr_contains': 'Використання: vm.sh БАЗА В1 В2 В3'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_07(case):
    lab03.check(V, case)
