"""Автоматична перевірка варіанта 12."""
import pytest
from conftest import load
from kits import lab03

V = load(12)
CASES = [{'id': 'успішне створення',
  'public': True,
  'kind': 'vm',
  'args': ['20G', 'base.qcow2'],
  'files': {'base.qcow2': {'text': 'fake', 'age_days': 1}},
  'stdout': 'Створено overlay 20G на базі base.qcow2\n',
  'code': 0,
  'images': {'ci-overlay.qcow2': {'format': 'qcow2',
                                  'virtual-size': 21474836480,
                                  'backing': 'base.qcow2',
                                  'backing-format': 'qcow2'}}},
 {'id': 'базовий образ відсутній',
  'public': True,
  'kind': 'vm',
  'args': ['20G', 'missing.qcow2'],
  'stdout': '',
  'code': 2,
  'stderr_contains': 'Помилка: базовий образ відсутній'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_12(case):
    lab03.check(V, case)
