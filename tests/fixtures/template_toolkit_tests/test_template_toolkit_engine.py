import os

from nose.tools import eq_
from moban.plugins import ENGINES, BaseEngine
from moban_template_toolkit.engine import EngineTemplateToolkit


def test_template_toolkit_eninge_type():
    engine = ENGINES.get_engine("template_toolkit", [], "")
    assert engine.engine_cls == EngineTemplateToolkit


def test_template_toolkit_template():
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "template_toolkit_tests")
    engine = BaseEngine(path, path, EngineTemplateToolkit)
    engine.render_to_file("template_tests.tt", "template_tests.json",
                          output)

    with open(output, "r") as output_file:
        expected_path = os.path.join("tests", "fixtures",
                                     "template_toolkit_tests",
                                     "expected_output.txt")
        with open(expected_path) as expected_file:
            expected_output = expected_file.read()
            rendered_output = output_file.read()
            eq_(rendered_output, expected_output)
    os.unlink(output)
