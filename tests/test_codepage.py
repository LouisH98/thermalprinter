#!/usr/bin/python3
# coding: utf-8

import pytest

from ..constants import CodePage
from ..exceptions import ThermalPrinterConstantError


def test_default_value(printer):
        assert printer._codepage is CodePage.CP437


def test_changing_no_value(printer):
        printer.codepage()
        assert printer._codepage is CodePage.CP437


def test_changing_good_value(printer):
        printer.codepage(CodePage.ISO_8859_1)
        assert printer._codepage is CodePage.ISO_8859_1


def test_changing_bad_value(printer):
        with pytest.raises(ThermalPrinterConstantError):
            printer.codepage('42')