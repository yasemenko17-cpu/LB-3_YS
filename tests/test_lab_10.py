"""Автоматична перевірка варіанта 10."""
import pytest
from conftest import load
from kits import lab03

V = load(10)
CASES = [{'id': 'успіх medium',
  'public': True,
  'kind': 'vm',
  'args': ['web.qcow2', 'medium'],
  'stdout': 'Образ web.qcow2 розміром 30 G створено\n',
  'code': 0,
  'images': {'web.qcow2': {'format': 'qcow2',
                           'virtual-size': 32212254720,
                           'backing': None,
                           'backing-format': None}}},
 {'id': 'невідомий тип',
  'public': True,
  'kind': 'vm',
  'args': ['web.qcow2', 'huge'],
  'stdout': '',
  'code': 2,
  'stderr_contains': 'Помилка: невідомий тип'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_10(case):
    lab03.check(V, case)
