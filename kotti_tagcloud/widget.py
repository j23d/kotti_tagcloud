from pyramid.events import subscriber
from pyramid.exceptions import PredicateMismatch
from pyramid.view import view_config

from kotti.resources import Tag
from kotti.views.slots import assign_slot

from kotti_settings.events import SettingsAfterSave
from kotti_settings.util import get_setting
from kotti_settings.util import remove_from_slots
from kotti_settings.util import show_in_context


@view_config(name='tagcloud-widget',
             renderer='kotti_tagcloud:templates/tagcloud.pt')
def tagcloud_widget(context, request):
    show = show_in_context(get_setting(u'show_in_context'), context)
    if show:
        tags = Tag.query.all()
        if tags:
            from kotti_tagcloud.fanstatic import tagcloud
            tagcloud.need()
            return {'tags': tags}
    raise(PredicateMismatch)


@subscriber(SettingsAfterSave)
def set_assigned_slot(event):
    """Reset the widget to the choosen slot."""

    # Check if the settings for this module was saved.
    if not event.module == __package__:
        return

    slot = get_setting('slot', u'left')
    remove_from_slots('tagcloud-widget')
    assign_slot('tagcloud-widget', slot)


def includeme(config):
    config.scan(__name__)
    config.add_translation_dirs('kotti_tagcloud:locale')
