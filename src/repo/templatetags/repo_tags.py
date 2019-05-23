from django import template

register = template.Library()


@register.inclusion_tag('repo/tags/messages.html', takes_context=True)
def show_messages(context, show=True):
    return {'messages': (context.get('messages') if show else None)}
