from jinja2 import Environment, FileSystemLoader

class CustomEnvironment(Environment): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loader = FileSystemLoader('templates')

    def get_template(self, name, parent=None, globals=None):
        if not name.endswith('.html'):
            name += '.html'
        return super().get_template(name, parent, globals)
    
def environment(**options):
    env = CustomEnvironment(
        loader=FileSystemLoader('arrienda_rural/front/assets/templates'),
        **options
    )
    env.globals.update({
        'static': 'django.templatetags.static.static',
        'url': 'django.urls.reverse',
    })
    return env