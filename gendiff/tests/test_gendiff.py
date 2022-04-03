from gendiff.scripts.gendiff import gendifference


def test_two_fixtured_files():
    assert gendifference(['./gendiff/tests/fixtures/file1.json', './gendiff/tests/fixtures/file2.json']) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_two_YAML_files():
    assert gendifference(['./gendiff/tests/fixtures/filepath1.yml', './gendiff/tests/fixtures/filepath2.yml']) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_two_fractal_json_files():
    assert gendifference(['./gendiff/tests/fixtures/file11.json', './gendiff/tests/fixtures/file12.json']) == '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
