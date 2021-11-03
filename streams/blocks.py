"""StreamFields live in here"""
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)

from wagtail.core import blocks

from wagtail.core.fields import StreamField, RichTextField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


"""General blocks"""

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(self, required=True, help_text=None, editor="default", features=None, **kwargs):
        # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=True, max_length=60)
    text = SimpleRichtextBlock(required=False, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class LinkStructValue(blocks.StructValue):
    """Additional logic for our urls."""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None

    # def latest_posts(self):
    #     return BlogDetailPage.objects.live()[:3]


class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""

    button_title = blocks.CharBlock(required=False, max_length=60)
    button_text = RichtextBlock(required=False, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page')

    class Meta:  # noqa
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue


class TitleAndTextBlock(blocks.StructBlock):
    """title and text and nothing else"""
    title = blocks.CharBlock(required=True, help_text='Add Your Title')
    text = blocks.CharBlock(required=True, help_text='Add Additional Text')

    class Meta: # noga
        #template = "streams/title_and_text_block.html"
        icon ='edit'
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Expo Cards"


class DateBlock(blocks.StructBlock):
    date = blocks.DateBlock(required=False)


class CarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock(blank=True)

    class Meta:
        template = 'streams/carousel_block.html'



class PromoBlock(blocks.StructBlock):
    bio = SimpleRichtextBlock(required=False,)
    pitch = SimpleRichtextBlock(help_text='Optional', required=False,)

    class Meta: #noga
        template = "streams/promo_block.html"
        icon = 'placeholder'
        label = "Dates"


class CoverImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(null=True, blank=True)
    teaser = RichtextBlock(null=True, blank=True, features=['h1', 'h2', 'h3', 'h4', "bold", "italic"])
    sub_teaser = RichtextBlock(null=True, blank=True, features=['h4', 'h5', 'h6', "bold", "italic"])
    #text = RichTextField(features=['h1', 'h2', 'h3', 'h4', "bold", "italic"])

    class Meta:  # noqa
        template = "streams/cover_image_block.html"
        icon = "placeholder"
        label = "Cover"