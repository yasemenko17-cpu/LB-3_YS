"""Автоматична перевірка варіанта 29."""
import pytest
from conftest import load
from kits import lab03

V = load(29)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['10'],
  'stdout': 'Шлюз: 10 G\n',
  'code': 0,
  'images': {'router.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240}}},
 {'id': 'межа: 5 ГБ',
  'public': True,
  'kind': 'vm',
  'args': ['5'],
  'stdout': 'Шлюз: 5 G\n',
  'code': 0,
  'images': {'router.qcow2': {'format': 'qcow2', 'virtual-size': 5368709120}}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_29(case):
    lab03.check(V, case)
