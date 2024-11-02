from django.forms import widgets
from django.utils.safestring import mark_safe
import crispy_bootstrap5

class CustomPicImgFieldWidget(widgets.FileInput):
    # here we descide the type of fields that we want to change it's widget property
    def render(self, name, value, attrs=None, **kwargs):
        default_html = super().render(name, value, attrs, **kwargs)
        if value:
            img_html = mark_safe(f'<img src="{value.url}"  width="200" />')
            return f'{img_html}{default_html}'
        else:
            return default_html
