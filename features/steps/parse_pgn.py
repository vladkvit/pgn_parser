import pgn
from pgn_parser import Actions
from behave import given, when, then
from hamcrest import assert_that, has_item, equal_to


@given(u'a pgn file with only a header of the tag pairs {tag_pairs}')
def step_a_pgn_file_with_tag_pair(context, tag_pairs):
    context.pgn_str = tag_pairs.replace("\\n", "\n")


@when(u'we parse it')
def step_we_parse_it(context):
    context.pgn = pgn.parse(context.pgn_str, actions=Actions())


@then(u'we can access a TagPair of k {tag_key}, v {tag_value}')
def step_we_can_access_a_TagPair(context, tag_key, tag_value):
    assert_that(context.pgn.tag_pairs, has_item(tag_key))
    assert_that(context.pgn.tag_pairs[tag_key], equal_to(tag_value))


@then(u'we can access a fully populated TagPairs dict {tp_res}')
def step_we_can_access_tagpairs(context, tp_res):
    TEST_TP_RES = {
        "TEST_TP_2_RES": {"Event": "Let's Play!", "Site": "Chess.com"},
        "TEST_TP_3_RES": {"Event": "Let's Play!", "Site": "Chess.com", "Date": "2018.12.13"}}
    r = TEST_TP_RES[tp_res]
    for k in r.keys():
        assert_that(context.pgn.tag_pairs, has_item(k))
        assert_that(context.pgn.tag_pairs[k], equal_to(r[k]))

@given(u'a pgn file with only movetext {movetext}')
def step_a_movetext_only_pgn(context, movetext):
    context.pgn_str = movetext.replace("\\n", "\n")


@then(u'we can access the moves node containing an array of correct Move objects with {sans}')
def step_we_can_access_moves(context, sans):
    for i, san in enumerate(sans.split(',')):
        assert_that(context.pgn.moves[0].san, equal_to(san))
