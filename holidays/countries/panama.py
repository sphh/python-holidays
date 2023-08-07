#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td

from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Panama(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Panama
      - https://publicholidays.com.pa/
    """

    country = "PA"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date) -> None:
        if self.observed and self._is_sunday(dt):
            self._add_holiday("%s (Observed)" % self[dt], dt + td(days=+1))

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Martyrs' Day
        self._add_observed(self._add_holiday_jan_9("Martyrs' Day"))

        # Carnival
        self._add_carnival_tuesday("Carnival")

        # Good Friday
        self._add_good_friday("Good Friday")

        # Labour Day
        self._add_observed(self._add_labor_day("Labour Day"))

        # Separation Day
        self._add_holiday_nov_3("Separation Day")

        # National Symbols Day
        self._add_holiday_nov_4("National Symbols Day")

        # Colon Day
        self._add_holiday_nov_5("Colon Day")

        # Los Santos Uprising Day
        self._add_holiday_nov_10("Los Santos Uprising Day")

        # Independence Day
        self._add_observed(self._add_holiday_nov_28("Independence Day"))

        # Mother's Day
        self._add_observed(self._add_holiday_dec_8("Mother's Day"))

        # National Mourning Day
        if year >= 2022:
            self._add_observed(self._add_holiday_dec_20("National Mourning Day"))

        # Christmas Day
        self._add_observed(self._add_christmas_day("Christmas Day"))


class PA(Panama):
    pass


class PAN(Panama):
    pass