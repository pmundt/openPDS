from django import template
from django.conf import settings
import pystache
import os

register = template.Library()

class View(pystache.TemplateSpec):
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    renderer = pystache.Renderer(search_dirs = template_path)

    def __init__(self, template_name, context):
        self.template_name = template_name

    def render(self):
	return self.renderer.render(self)

class MustacheNode(template.Node):
    def __init__(self, template_path, attr=None):
        self.template = template_path
        self.attr = attr

    def render(self, context):
        mcontext = context[self.attr] if self.attr else {}
        view = View(self.template, context=mcontext)
        return view.render()

def do_mustache(parser, token):
    """
    Loads a mustache template and render it inline
    
    Example::
    
    {% mustache "foo/bar" data %}
    
    """
    bits = token.split_contents()
    if len(bits) not in  [2,3]:
        raise template.TemplateSyntaxError("%r tag takes two arguments: the location of the template file, and the template context" % bits[0])
    path = bits[1]
    path = path[1:-1]
    attrs = bits[2:]
    return MustacheNode(path, *attrs)


register.tag("mustache", do_mustache)
