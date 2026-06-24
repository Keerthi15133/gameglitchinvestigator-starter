import contextlib
import importlib
import os
import sys
from types import SimpleNamespace

import pytest
import streamlit as st

# Ensure project root is on sys.path so tests can import modules from it
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high():
    # If secret is 50 and guess is 60, it should return a down hint
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")


def test_guess_too_low():
    # If secret is 50 and guess is 40, it should return an up hint
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_new_game_resets_status_and_history(monkeypatch):
    # Simulate clicking the New Game button after a lost round
    class DummySessionState(dict):
        def __getattr__(self, name):
            return self[name]

        def __setattr__(self, name, value):
            self[name] = value

        def __delattr__(self, name):
            del self[name]

    dummy_state = DummySessionState(
        status="lost",
        history=[94, 37],
        attempts=8,
        secret=94,
    )

    monkeypatch.setattr(st, "session_state", dummy_state, raising=False)
    monkeypatch.setattr(st, "set_page_config", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "title", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "caption", lambda *args, **kwargs: None)
    monkeypatch.setattr(
        st,
        "sidebar",
        SimpleNamespace(
            header=lambda *args, **kwargs: None,
            selectbox=lambda *args, **kwargs: "Normal",
            caption=lambda *args, **kwargs: None,
        ),
        raising=False,
    )
    monkeypatch.setattr(st, "subheader", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "info", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "expander", lambda *args, **kwargs: contextlib.nullcontext())
    monkeypatch.setattr(st, "write", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "text_input", lambda *args, **kwargs: "")
    monkeypatch.setattr(st, "columns", lambda n: (contextlib.nullcontext(),) * n)
    monkeypatch.setattr(st, "button", lambda label: label == "New Game 🔁")
    monkeypatch.setattr(st, "checkbox", lambda *args, **kwargs: False)
    monkeypatch.setattr(st, "success", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "error", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "warning", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "balloons", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "divider", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "rerun", lambda: None)
    monkeypatch.setattr(st, "stop", lambda: None)

    sys.modules.pop("app", None)
    import app
    importlib.reload(app)

    assert st.session_state.status == "playing"
    assert st.session_state.history == []
