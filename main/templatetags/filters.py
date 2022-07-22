from django import template

register = template.Library()

@register.filter
def source(index):
	return channels_list[int(index)]