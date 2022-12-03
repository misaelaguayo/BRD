import io
from unittest import TestCase, mock
from src.Brd import Brd


class Tests(TestCase):
    def setUp(self):
        self.brd = Brd()

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        self.brd.runFile(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_block_scope(self):
        self.assert_stdout(
            "examples/block_scope.brd",
            "inner a\nouter b\nglobal c\nouter a\nouter b\nglobal c\nglobal a\nglobal b\nglobal c\n",
        )

    def test_printing(self):
        self.assert_stdout(
            "examples/printing.brd",
            "one\ntrue\n3\n",
        )

    def test_variable_assignment(self):
        self.assert_stdout(
            "examples/variable_assignment.brd",
            "2\n",
        )

    def test_variables(self):
        self.assert_stdout(
            "examples/variables.brd",
            "3\n",
        )

    def test_while_stmt(self):
        self.assert_stdout(
            "examples/while_stmt.brd",
            "nil\n1\n2\n3\n4\n5\n6\n7\n8\n9\n",
        )
