from gendiff.scripts.gendiff import gendifference


def test_two_fixtured_files():
    assert gendifference(['./gendiff/tests/fixtures/file1.json', './gendiff/tests/fixtures/file2.json']) == '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

def test_two_YAML_files():
    assert gendifference(['./gendiff/tests/fixtures/filepath1.yml', './gendiff/tests/fixtures/filepath2.yml']) == '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''
