import ast
import codecs

from template import Template
from template.util import Literal
import moban.utils as utils 


class EngineTemplateToolkit(object):
	def __init__(self, template_dirs, extensions=None):
		self.template_dirs = template_dirs

	def get_template(self, template_file):
		actual_file = utils.get_template_path(
			self.template_dirs, template_file
		)

		with codecs.open(actual_file, "r",
			encoding="utf-8") as template_contents:

			source = Literal(template_contents.read())
		
		# Template-Toolkit-Python cannot make a Template Object only
        # by passing a file_name or file_content. It uses a function
        # process() to generate the template. The process function
        # needs to have both the template file and the data of the
        # variables used in template.
		template = []
		template_object = Template()
		template.append(template_object)
		template.append(source)

		return template

	def apply_template(self, template, data, output):
		template_object = template[0]
		source = template[1]
		rendered_content = template_object.process(source, data)
		return rendered_content


