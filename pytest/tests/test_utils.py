# coding=utf-8
"""
Test for the utility functions in Para-C (test_util.py and decorators.py)
"""
from pathlib import Path

import pytest

from parac import util


class TestValidateFileEnding:
    @pytest.mark.parametrize(
        "file", (
                "x.para",
                "y.parah",
                "z.c",
                "x.h",
                "y.ph"
        )
    )
    def test_valid(self, file):
        assert util.has_valid_file_ending(file)

    @pytest.mark.parametrize(
        "file", (
                "",
                "yparah",
                "z.x",
                "x.hex"
        )
    )
    def test_invalid(self, file):
        assert util.has_valid_file_ending(file) is False


class TestGetRelativeFileName:
    def test_assert_same_file_name(self):
        try:
            name = util.get_relative_file_name(
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
            name = util.get_relative_file_name(
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
        name = util.get_relative_file_name(
            file_name="name.para",
            file_path="/usr/name/files/name.para",
            base_path="/usr/name/files/"
        )
        assert name == "name"

    def test_nested_file(self):
        name = util.get_relative_file_name(
            file_name="second_name.para",
            file_path="/usr/name/files/name/second_name.para",
            base_path="/usr/name/files/"
        )
        assert name == "name.second_name"

    def test_double_nested_file(self):
        name = util.get_relative_file_name(
            file_name="second_name.para",
            file_path="/usr/name/files/name/name2/name3/second_name.para",
            base_path="/usr/name/files/"
        )
        assert name == "name.name2.name3.second_name"

    def test_invalid_name(self):
        try:
            name = util.get_relative_file_name(
                file_name="na*me?.pa\\ra",
                file_path="/usr/name/files/name/second_name.para",
                base_path="/usr/name/files/"
            )
            assert name == "name.second_name"
        except RuntimeError:
            ...
        else:
            assert False

    def test_spaces(self):
        try:
            util.get_relative_file_name(
                file_name="name .para",
                file_path="/usr/name/files/name .para",
                base_path="/usr/name/files/"
            )
        except RuntimeError:
            ...
        else:
            assert False

        try:
            util.get_relative_file_name(
                file_name="name .para",
                file_path="/dir/name .para",
                base_path="/dir/"
            )
        except RuntimeError:
            ...
        else:
            assert False

        try:
            util.get_relative_file_name(
                file_name=" ",
                file_path="/dir/ ",
                base_path="/dir/"
            )
        except RuntimeError:
            ...
        else:
            assert False


class TestEnsurePathlibPath:
    @pytest.mark.parametrize(
        "file,expect", (
                ("path", Path("path").resolve()),
                ("path/path/path", Path("path/path/path").resolve()),
                ("./x/path/path", Path("./x/path/path").resolve()),
                ("../x/path/path", Path("../x/path/path").resolve())
        )
    )
    def test_str(self, file, expect):
        assert util.ensure_pathlib_path(file) == expect

    @pytest.mark.parametrize(
        "file,expect", (
                ("path".encode(), Path("path").resolve()),
                ("path/path/path".encode(), Path("path/path/path").resolve()),
                ("./x/path/path".encode(), Path("./x/path/path").resolve()),
                ("../x/path/path".encode(), Path("../x/path/path").resolve())
        )
    )
    def test_bytes(self, file, expect):
        assert util.ensure_pathlib_path(file) == expect

    @pytest.mark.parametrize(
        "file,expect", (
                (Path("path"), Path("path").resolve()),
                (Path("path/path/path"), Path("path/path/path").resolve()),
                (Path("./x/path/path").resolve(),
                 Path("./x/path/path").resolve()),
                (Path("../x/path/path").resolve(),
                 Path("../x/path/path").resolve())
        )
    )
    def test_path(self, file, expect):
        assert util.ensure_pathlib_path(file) == expect
