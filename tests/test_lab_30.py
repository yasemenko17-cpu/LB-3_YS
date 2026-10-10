"""Автоматична перевірка варіанта 30."""
import pytest
from conftest import load
from kits import lab03

V = load(30)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['student.qcow2'],
  'stdout': 'Створено навчальний образ: student.qcow2\n',
  'code': 0,
  'images': {'student.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240}}},
 {'id': "інше ім'я",
  'public': True,
  'kind': 'vm',
  'args': ['test.qcow2'],
  'stdout': 'Створено навчальний образ: test.qcow2\n',
  'code': 0,
  'images': {'test.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240}}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_30(case):
    lab03.check(V, case)
