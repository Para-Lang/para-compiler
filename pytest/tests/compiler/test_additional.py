# coding=utf-8
""" Test for the extensions setup """
import pytest

from paralang_base.compiler import ParaCompiler


class TestAdditional:
    @pytest.mark.parametrize(
        "expected,input_str,line_ending", [
            ("x y z", "x y z", "\n"),
            ("x y z", "x y z", "\r\n"),
            ("x \ny z", "x // some \ny z", "\n"),
            ("x \r\ny z", "x // some \ny z", "\r\n"),
            ("\nx \ny \nz", "/* xx  */x // some \ny // x x x \r\nz", "\n"),
            ("\rx \ry \rz", "/* xx  */x // some \ny // x x x \r\nz", "\r"),
            ("x \n\n\ny z", "x // x \r// x \n// x \r\ny z", "\n"),
            ("x \r\r\ry z", "x // x \r// x \n// x \r\ny z", "\r"),
            ("x \n\n\n\ny \nz", "x // x \r\n\n// x \n// x \r\ny \nz", "\n"),
            ("x \r\r\r\ry \rz", "x // x \r\n\n// x \n// x \r\ny \nz", "\r"),
        ]
    )
    def test_remove_comments_from_str(
            self, expected: str, input_str: str, line_ending: str
    ):
        assert expected == ParaCompiler.remove_comments_from_str(
            input_str, line_ending
        )
