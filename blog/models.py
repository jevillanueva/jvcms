from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.blocks import RawHTMLBlock
from wagtail.search import index
from wagtailmarkdown.fields import MarkdownField
from wagtail.images.edit_handlers import ImageChooserPanel
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    particle_param = StreamField([
            ('param', RawHTMLBlock(required=False)),
    ], blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        StreamFieldPanel('particle_param'),
    ]


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    imagePage = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    imageBanner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    contentMarkdown = MarkdownField(blank=True)

    externalRaws = StreamField([
        ('external', blocks.StructBlock([
            ('rawHTML', RawHTMLBlock(required=False)),
            ('rawImportScriptCSSAndMeta', RawHTMLBlock(required=False,
             help_text="https://www.npmjs.com/package/react-helmet#reference-guide")),
            ('rawScripts', RawHTMLBlock(required=False)),
            ('rawScriptsBabel', RawHTMLBlock(required=False)),
        ])),
    ], blank=True)
    particle_param = StreamField([
            ('param', RawHTMLBlock(required=False)),
    ], blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        ImageChooserPanel('imagePage'),
        ImageChooserPanel('imageBanner'),
        FieldPanel('body', classname="full"),
        FieldPanel('contentMarkdown', classname="full"),
        StreamFieldPanel('externalRaws'),
        StreamFieldPanel('particle_param'),
    ]