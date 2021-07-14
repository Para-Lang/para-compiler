# coding=utf-8
"""
Test for the utility functions in Para-C (test_utils.py and decorators.py)
"""

from paraccompiler import utils, WIN


class TestCheckValidPathName:
    def test_simple_assert(self):
        assert utils.check_valid_path_name(
            "dest/temp/name.para",
        )

    def test_wrong_path(self):
        if WIN:
            assert not utils.check_valid_path_name(
                "/dest*/na*me?.pa\\ra",
            )
        else:
            assert not utils.check_valid_path_name(
                "/dest/&name.para",
            )

    def test_valid_path(self):
        assert utils.check_valid_path_name(
            "/dest/name.para",
        )

    def test_wrong_name(self):
        if WIN:
            assert not utils.check_valid_path_name(
                "na*me?.pa\\ra",
            )
        else:
            assert not utils.check_valid_path_name(
                "name.pa&ra",
            )

    def test_valid_name(self):
        assert utils.check_valid_path_name(
            "name.para",
        )

    def test_win_path(self):
        assert utils.check_valid_path_name(
            "D:\\name.para",
            win_path=True
        )

        assert utils.check_valid_path_name(
            "\\dest\\name.para",
        )


class TestGetRelativeFileName:
    def test_assert_same_file_name(self):
        try:
            name = utils.get_relative_file_name(
                file_name="name.para",
                file_path="/usr/name/files/name/second_name.para",
                base_path="/usr/name/files/"
            )
            assert name == "name.second_name"
        except RuntimeError:
            ...
        else:
            assert False

    def test_mismatching_paths(self):
        try:
            name = utils.get_relative_file_name(
                file_name="name.para",
                file_path="/usr/name/files/name/second_name.para",
                base_path="/usr/bin/content/"
            )
            assert name == "name.second_name"
        except RuntimeError:
            ...
        else:
            assert False

    def test_simple_entry_file_path(self):
        name = utils.get_relative_file_name(
            file_name="name.para",
            file_path="/usr/name/files/name.para",
            base_path="/usr/name/files/"
        )
        assert name == "name"

    def test_nested_file(self):
        name = utils.get_relative_file_name(
            file_name="second_name.para",
            file_path="/usr/name/files/name/second_name.para",
            base_path="/usr/name/files/"
        )
        assert name == "name.second_name"

    def test_double_nested_file(self):
        name = utils.get_relative_file_name(
            file_name="second_name.para",
            file_path="/usr/name/files/name/name2/name3/second_name.para",
            base_path="/usr/name/files/"
        )
        assert name == "name.name2.name3.second_name"

    def test_invalid_name(self):
        try:
            name = utils.get_relative_file_name(
                file_name="na*me?.pa\\ra",
                file_path="/usr/name/files/name/second_name.para",
                base_path="/usr/name/files/"
            )
            assert name == "name.second_name"
        except RuntimeError:
            ...
        else:
            assert False

    def test_win(self):
        name = utils.get_relative_file_name(
            file_name="entry.para",
            file_path="D:\\dir\\entry.para",
            base_path="D:\\dir\\",
            win_path=True
        )
        assert name == "entry"

        name = utils.get_relative_file_name(
            file_name="entry.para",
            file_path="D:\\dir\\x\\entry.para",
            base_path="D:\\dir\\",
            win_path=True
        )
        assert name == "x.entry"

    def test_spaces(self):
        try:
            name = utils.get_relative_file_name(
                file_name="name .para",
                file_path="/usr/name/files/name .para",
                base_path="/usr/name/files/"
            )
        except RuntimeError:
            ...
        else:
            assert False

        try:
            name = utils.get_relative_file_name(
                file_name="name .para",
                file_path="/dir/name .para",
                base_path="/dir/"
            )
        except RuntimeError:
            ...
        else:
            assert False

        try:
            name = utils.get_relative_file_name(
                file_name=" ",
                file_path="/dir/ ",
                base_path="/dir/"
            )
        except RuntimeError:
            ...
        else:
            assert False

        try:
            name = utils.get_relative_file_name(
                file_name=" ",
                file_path="\\dir\\name.para",
                base_path="D:\\dir\\",
                win_path=True
            )
        except RuntimeError:
            ...
        else:
            assert False
