"""Автоматична перевірка варіанта 28."""
import pytest
from conftest import load
from kits import lab03

V = load(28)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['10', '100'],
  'stdout': 'ОС: 10 G, Дані: 100 G\n',
  'code': 0,
  'images': {'os.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240},
             'storage.raw': {'format': 'raw', 'virtual-size': 107374182400}}},
 {'id': 'інші розміри',
  'public': True,
  'kind': 'vm',
  'args': ['20', '200'],
  'stdout': 'ОС: 20 G, Дані: 200 G\n',
  'code': 0,
  'images': {'os.qcow2': {'format': 'qcow2', 'virtual-size': 21474836480},
             'storage.raw': {'format': 'raw', 'virtual-size': 214748364800}}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_28(case):
    lab03.check(V, case)
