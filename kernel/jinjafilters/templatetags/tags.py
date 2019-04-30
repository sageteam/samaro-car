from django import template
from khayyam import JalaliDate
from khayyam import JalaliDatetime


register = template.Library()


@register.filter(name = 'jalali_date')
def persian_date(date):
    return JalaliDate(date).strftime('%n-%m-%K')

@register.filter(name = 'jalali_date_2')
def persian_date_2(date):
    return JalaliDate(date).strftime('%K-%R-%n')


@register.filter(name = 'jalali_time')
def persian_time(date):
    return JalaliDatetime(date).strftime('%k:%r')
