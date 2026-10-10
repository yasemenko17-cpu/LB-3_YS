"""Автоматична перевірка варіанта 15."""
import pytest
from conftest import load
from kits import lab03

V = load(15)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['8G'],
  'stdout': 'Створено диск: 8G\n',
  'code': 0,
  'images': {'edu-disk.qcow2': {'format': 'qcow2', 'virtual-size': 8589934592}}},
 {'id': 'нульовий розмір',
  'public': True,
  'kind': 'vm',
  'args': ['0G'],
  'stdout': '',
  'code': 2,
  'stderr_contains': 'Помилка: нульовий розмір'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_15(case):
    lab03.check(V, case)
