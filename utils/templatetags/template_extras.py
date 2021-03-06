from django import template

from utils import misc_functions

register = template.Library()
register.filter('format_decimal'      , misc_functions.format_decimal)
register.filter('format_dollar_amount', misc_functions.format_dollar_amount)
register.filter('format_date'         , misc_functions.format_date)
register.filter('format_date_time'    , misc_functions.format_date_time)
register.filter('index1_in'           , misc_functions.index1_in)
register.filter('utc_to_local'        , misc_functions.utc_to_local)

register.filter('format_dollar_amount_neg',
  lambda x: misc_functions.format_dollar_amount(x, True))
