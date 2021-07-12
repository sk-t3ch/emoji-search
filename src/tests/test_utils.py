import pytest
import json
import pathlib
import fastjsonschema
BASE = pathlib.Path(__file__).parent.parent
SCHEMA = BASE.joinpath("schema")


def load_schema(reference):
    json_data = json.loads(open(SCHEMA.joinpath(
        reference).absolute().as_posix(), 'rb').read().decode('utf-8'))
    return {
        "compiled": fastjsonschema.compile(json_data),
        "raw": json_data
    }

schemas = {
    'input': load_schema('input.json'),
    'output': load_schema('output.json'),
}

def test_input_schema_correct():
    input = { "search": "blah blah blah", "key": "123"}
    schemas["input"]["compiled"](input)

@pytest.mark.xfail(raises=Exception)
def test_input_schema_fails():
    input = { "key": "123"}
    schemas["input"]["compiled"](input)

def test_output_schema_correct():
    output = { "most_similar": [{"emoji": "a", "code_point": [123], "description": "blah", "score": 0.3}]}
    schemas["output"]["compiled"](output)


@pytest.mark.xfail(raises=Exception)
def test_output_schema_fails():
    output = { "most_similar": [{"code_point": [123], "description": "blah", "score": 0.3}]}
    schemas["output"]["compiled"](output)