# https://stash.ihme.washington.edu/projects/VA/repos/business_rules/browse/doc/md/cancer.md
from smartva.data.constants import *
from smartva.utils.utils import value_from_row, int_or_float

CAUSE_ID = 12


def logic_rule(row):
    value_of = value_from_row(row, int_or_float)

    return value_of(Child.FREE_TEXT_CANCER) == YES
