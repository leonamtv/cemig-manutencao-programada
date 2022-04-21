from unittest import TestCase

from src.core.util import filter_city_name, non_null


class TestFilterCityName(TestCase):
    def test_filter_city_name_case_A(self):
        self.assertEqual(filter_city_name('Timóteo'), 'TIMOTEO')

    def test_filter_city_name_case_B(self):
        self.assertEqual(filter_city_name('BÁNÃNÀ'), 'BANANA')

    def test_filter_city_name_case_C(self):
        self.assertEqual(filter_city_name('banana'), 'BANANA')

    def test_filter_city_name_case_D(self):
        self.assertEqual(filter_city_name('á'), 'A')


class TestNonNull(TestCase):
    def test_non_null_when_none(self):
        self.assertFalse(non_null(None))

    def test_non_null_when_nan_case_A(self):
        self.assertFalse(non_null('nan'))

    def test_non_null_when_nan_case_B(self):
        self.assertFalse(non_null('nAn'))

    def test_non_null_when_nan_case_C(self):
        self.assertFalse(non_null('NaN'))

    def test_non_null_when_null_case_A(self):
        self.assertFalse(non_null('null'))

    def test_non_null_when_null_case_B(self):
        self.assertFalse(non_null('Null'))

    def test_non_null_when_null_case_C(self):
        self.assertFalse(non_null('NULL'))
