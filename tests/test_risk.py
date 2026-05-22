"""Tests for risk guardrails."""

from promptrader.risk import Risk


def test_drawdown_not_hit():
    r = Risk(max_drawdown=0.10)
    assert r.check_drawdown(current_equity=950, starting_equity=1000) is False


def test_drawdown_hit():
    r = Risk(max_drawdown=0.10)
    assert r.check_drawdown(current_equity=900, starting_equity=1000) is True


def test_drawdown_zero_start_safe():
    r = Risk(max_drawdown=0.10)
    assert r.check_drawdown(current_equity=0, starting_equity=0) is False


def test_position_size_within():
    r = Risk(max_position_size=0.10)
    assert r.check_position_size(position_value=50, equity=1000) is False


def test_position_size_exceeds():
    r = Risk(max_position_size=0.10)
    assert r.check_position_size(position_value=200, equity=1000) is True


def test_token_budget_none_uncapped():
    r = Risk(token_budget_usd=None)
    assert r.check_token_budget(spent_usd=99999) is False


def test_token_budget_hit():
    r = Risk(token_budget_usd=10.0)
    assert r.check_token_budget(spent_usd=11.0) is True
