"""Автоматична перевірка варіанта 26."""
import pytest
from conftest import load
from kits import lab03

V = load(26)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['10', '50'],
  'stdout': 'Створено sys.raw на 10 G\nСтворено data.qcow2 на 50 G\n',
  'code': 0,
  'images': {'sys.raw': {'format': 'raw', 'virtual-size': 10737418240},
             'data.qcow2': {'format': 'qcow2', 'virtual-size': 53687091200}}},
 {'id': 'інші розміри',
  'public': True,
  'kind': 'vm',
  'args': ['20', '100'],
  'stdout': 'Створено sys.raw на 20 G\nСтворено data.qcow2 на 100 G\n',
  'code': 0,
  'images': {'sys.raw': {'format': 'raw', 'virtual-size': 21474836480},
             'data.qcow2': {'format': 'qcow2', 'virtual-size': 107374182400}}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_26(case):
    lab03.check(V, case)
