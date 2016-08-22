"""Tests for sqlalchemy orm session."""

import astroid

from sqlalchemy.orm.scoping import scoped_session

from unittest import TestCase


class PluginTest(TestCase):
    """PluginTest test case."""

    def setUp(self):
        """Init setup."""
        self.node = astroid.MANAGER.ast_from_class(
            scoped_session, scoped_session.__module__
        )

    def tearDown(self):
        """Tear down."""
        pass

    def test_node(self):
        """Test the node."""
        self.assertIsNotNone(self.node)
        self.assertIsInstance(
            self.node.getattr('query')[0], astroid.FunctionDef
        )
        self.assertIsInstance(
            self.node.getattr('add')[0], astroid.FunctionDef
        )
