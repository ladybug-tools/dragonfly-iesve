"""Test the CLI commands"""
import os
from click.testing import CliRunner

from dragonfly_iesve.cli.translate import model_to_gem_cli


def test_df_model_to_ies():
    runner = CliRunner()
    input_df_model = './tests/assets/simple_model.dfjson'
    output_gem = './tests/assets/simple_model.gem'

    in_args = [input_df_model, '--output-file', output_gem]
    result = runner.invoke(model_to_gem_cli, in_args)
    assert result.exit_code == 0
    assert os.path.isfile(output_gem)
    os.remove(output_gem)


def test_invalid_df_model_to_ies():
    runner = CliRunner()
    input_df_model = './tests/assets/model_invalid_adj.dfjson'
    output_gem = './tests/assets/model_invalid_adj.gem'

    in_args = [input_df_model, '--output-file', output_gem]
    result = runner.invoke(model_to_gem_cli, in_args)
    assert result.exit_code == 0
    assert os.path.isfile(output_gem)
    os.remove(output_gem)
