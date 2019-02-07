# flake8: noqa
from lml.plugin import PluginInfo, PluginInfoChain
import moban.constants as constants

from moban_template_toolkit._version import __version__
from moban_template_toolkit._version import __author__

PluginInfoChain(__name__).add_a_plugin_instance(
	PluginInfo(
		constants.TEMPLATE_ENGINE_EXTENSION,
		"%s.engine.EngineTemplateToolkit" % __name__,
		tags=["template_toolkit", "tt"]
	)
)
