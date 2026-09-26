from project import filter_time, filter_theme, filter_specialty

import pytest

def main():
    test_filter_time()
    test_filter_theme()
    test_filter_specialty()


def test_filter_time():
    assert filter_time("A") == ['Sunrise Cafe', 'Meow & Mocha']
    assert filter_time("D") == ['Sunrise Cafe', 'The Cozy Cup', 'The Rustic Bean', 'The Daily Grind', 'Coffee Canvas',
                                           'Byte & Bean', 'Meow & Mocha', "Tabby's Teahouse", 'Matcha Break', 'The Timeless Teapot']
    assert filter_time("E") == ['Sunrise Cafe', 'The Cozy Cup', 'The Rustic Bean', 'The Daily Grind', 'Coffee Canvas',
                                           'Byte & Bean', 'Meow & Mocha', "Tabby's Teahouse", 'Matcha Break', 'The Timeless Teapot']


def test_filter_theme():
    assert filter_theme("D") == ['Meow & Mocha', "Tabby's Teahouse"]
    assert filter_theme("C") == ['The Daily Grind', "Byte & Bean"]
    assert filter_theme("F") == ['Sunrise Cafe', 'The Cozy Cup', 'The Rustic Bean', 'The Daily Grind', 'Coffee Canvas',
                                           'Byte & Bean', 'Meow & Mocha', "Tabby's Teahouse", 'Matcha Break', 'The Timeless Teapot']


def test_filter_specialty():
    assert filter_specialty("B") == ['Meow & Mocha', 'The Timeless Teapot']
    assert filter_specialty("C") == ['The Rustic Bean', 'Coffee Canvas']
    assert filter_specialty("E") == ['Sunrise Cafe', 'The Cozy Cup', 'The Rustic Bean', 'The Daily Grind', 'Coffee Canvas',
                                           'Byte & Bean', 'Meow & Mocha', "Tabby's Teahouse", 'Matcha Break', 'The Timeless Teapot']


if __name__ == "__main__":
    main()