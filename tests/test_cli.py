import pytest

from fibonacci_kata.cli import build_parser, main


def test_parser_accepts_single_number():
    args = build_parser().parse_args(["10"])
    assert args.n == 10


def test_main_prints_single_value(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["n", "6"])
    main()
    assert capsys.readouterr().out.strip() == "8"


def test_main_requires_an_argument(monkeypatch):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata"])
    with pytest.raises(SystemExit):
        main()
