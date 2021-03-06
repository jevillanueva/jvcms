from pyexpat import model
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.blocks import RawHTMLBlock


class PortafolioIndex(Page):
    date = models.DateField("Post date")
    name = RichTextField(blank=True)
    jobTitle = RichTextField(blank=True)
    email = models.EmailField(blank=False)
    phone = models.TextField(blank=True)
    summary = RichTextField(blank=True)
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    orderData = StreamField([
        ('order', blocks.StructBlock([
            ('block', blocks.ChoiceBlock(required=True, choices=[
                ('employ', 'Employ'),
                ('certifications', 'Certifications'),
                ('courses', 'Courses'),
                ('extras', 'Extras'),
                ('skills', 'Skills'),
                ('publications', 'Publications'),
            ])),
        ])),
    ], blank=True)

    employ = StreamField([
        ('employ', blocks.StructBlock([
            ('jobTitle', blocks.CharBlock()),
            ('employer', blocks.CharBlock(required=False)),
            ('city', blocks.CharBlock(required=False)),
            ('description', blocks.RichTextBlock(required=False)),
            ('link', blocks.URLBlock(required=False)),
            ('initDate', blocks.DateBlock(required=False)),
            ('endDate', blocks.DateBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('document', DocumentChooserBlock(required=False)),
            ('rawHTML', RawHTMLBlock(required=False)),
            ('rawImportScriptCSSAndMeta', RawHTMLBlock(required=False,
             help_text="https://www.npmjs.com/package/react-helmet#reference-guide")),
        ])),
    ], blank=True)

    certifications = StreamField([
        ('certifications', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('institution', blocks.CharBlock(required=False)),
            ('description', blocks.RichTextBlock(required=False)),
            ('link', blocks.URLBlock(required=False)),
            ('initDate', blocks.DateBlock(required=False)),
            ('endDate', blocks.DateBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('document', DocumentChooserBlock(required=False)),
            ('rawHTML', RawHTMLBlock(required=False)),
            ('rawImportScriptCSSAndMeta', RawHTMLBlock(required=False,
             help_text="https://www.npmjs.com/package/react-helmet#reference-guide")),
        ])),
    ], blank=True)

    courses = StreamField([
        ('courses', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('institution', blocks.CharBlock(required=False)),
            ('description', blocks.RichTextBlock(required=False)),
            ('link', blocks.URLBlock(required=False)),
            ('initDate', blocks.DateBlock(required=False)),
            ('endDate', blocks.DateBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('document', DocumentChooserBlock(required=False)),
            ('rawHTML', RawHTMLBlock(required=False)),
            ('rawImportScriptCSSAndMeta', RawHTMLBlock(required=False,
             help_text="https://www.npmjs.com/package/react-helmet#reference-guide")),
        ])),
    ], blank=True)

    extras = StreamField([
        ('extras', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('site', blocks.CharBlock(required=False)),
            ('description', blocks.RichTextBlock(required=False)),
            ('link', blocks.URLBlock(required=False)),
            ('initDate', blocks.DateBlock(required=False)),
            ('endDate', blocks.DateBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('document', DocumentChooserBlock(required=False)),
            ('rawHTML', RawHTMLBlock(required=False)),
            ('rawImportScriptCSSAndMeta', RawHTMLBlock(required=False,
             help_text="https://www.npmjs.com/package/react-helmet#reference-guide")),
        ])),
    ], blank=True)

    skills = StreamField([
        ('skills', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.RichTextBlock(required=False)),
            ('link', blocks.URLBlock(required=False)),
            ('rawHTML', RawHTMLBlock(required=False)),
            ('rawImportScriptCSSAndMeta', RawHTMLBlock(required=False,
             help_text="https://www.npmjs.com/package/react-helmet#reference-guide")),
        ])),
    ], blank=True)

    publications = StreamField([
        ('publications', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.RichTextBlock(required=False)),
            ('link', blocks.URLBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('document', DocumentChooserBlock(required=False)),
            ('rawHTML', RawHTMLBlock(required=False)),
            ('rawImportScriptCSSAndMeta', RawHTMLBlock(required=False,
             help_text="https://www.npmjs.com/package/react-helmet#reference-guide")),
        ])),
    ], blank=True)
    particle_param = StreamField([
            ('param', RawHTMLBlock(required=False)),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name', classname="full"),
        FieldPanel('date'),
        FieldPanel('jobTitle'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('summary', classname="full"),
        ImageChooserPanel('profile_image'),
        StreamFieldPanel('orderData'),
        StreamFieldPanel('employ'),
        StreamFieldPanel('certifications'),
        StreamFieldPanel('courses'),
        StreamFieldPanel('extras'),
        StreamFieldPanel('skills'),
        StreamFieldPanel('publications'),
        StreamFieldPanel('particle_param'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('jobTitle'),
        index.SearchField('email'),
        index.SearchField('phone'),
    ]
