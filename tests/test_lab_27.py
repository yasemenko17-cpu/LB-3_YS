"""Автоматична перевірка варіанта 27."""
import pytest
from conftest import load
from kits import lab03

V = load(27)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['15', '15'],
  'stdout': 'Створено base.qcow2 на 15 G та node.qcow2 на 15 G\n',
  'code': 0,
  'images': {'base.qcow2': {'format': 'qcow2', 'virtual-size': 16106127360},
             'node.qcow2': {'format': 'qcow2',
                            'virtual-size': 16106127360,
                            'backing': 'base.qcow2',
                            'backing-format': 'qcow2'}}},
 {'id': 'різні розміри',
  'public': True,
  'kind': 'vm',
  'args': ['20', '30'],
  'stdout': 'Створено base.qcow2 на 20 G та node.qcow2 на 30 G\n',
  'code': 0,
  'images': {'base.qcow2': {'format': 'qcow2', 'virtual-size': 21474836480},
             'node.qcow2': {'format': 'qcow2',
                            'virtual-size': 32212254720,
                            'backing': 'base.qcow2',
                            'backing-format': 'qcow2'}}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_27(case):
    lab03.check(V, case)
