from django import template

register = template.Library()

channels_list = ['@Axbarot_live', '@TYUZBEK', '@shopirlar', '@YOL_YOLAKAY', '@Salomatlik_sirlari', '@Samarqand_Samarqandliklar_24', '@Uznext', '@Ginekologiya']
channels_list.sort()

@register.filter
def source(index):
	return channels_list[int(index)]