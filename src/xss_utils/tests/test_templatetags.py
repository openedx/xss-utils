"""
Tests for templates tags.
"""

from django.http import HttpResponse
from django.template import Context, Template
from django.test import TestCase


class InterpolateHtmlFilterTest(TestCase):
    """ Class for interpolate_html filter escaping """
    def test_interpolate_html_escape_rendered(self):
        """ Verify interpolate_html filter escapes string with kwargs """
        context = Context({})
        template_to_render = Template(
            '{% load django_markup %}'
            '{% interpolate_html \"{s} message <script>alert(\'alert\')</script>{e}\" s="<p>"|safe e="</p>"|safe %}'
        )
        rendered_template = template_to_render.render(context)
        response = HttpResponse(rendered_template)

        self.assertContains(response, '&lt;script&gt;')
        self.assertContains(response, '<p>')
