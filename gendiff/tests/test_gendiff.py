from gendiff.scripts.gendiff import gendifference


def test_two_fixtured_files():
    print(type(open('./gendiff/tests/fixtures/file1.json')))
    assert gendifference(['./gendiff/tests/fixtures/file1.json', './gendiff/tests/fixtures/file2.json']) == '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''
