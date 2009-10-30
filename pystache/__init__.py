from pystache.template import Template

def render(template, context={}, **kwargs):
    context = context.copy()
    for key in kwargs:
        context[key] = kwargs[key]
    return Template(template, context).render()
