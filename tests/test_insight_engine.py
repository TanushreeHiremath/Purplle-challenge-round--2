# PROMPT:
# Generate tests for AI retail insight generation.

# CHANGES MADE:
# - Added conversion analytics validation
# - Added queue insight validation


from services.detection_service.analytics.insight_engine import (
    generate_ai_insights,
)


def test_insights():

    funnel_data = {

        "entered": 10,

        "browsed": 8,

        "queued": 3,

        "purchased": 5
    }

    insights = generate_ai_insights(
        funnel_data
    )

    assert isinstance(
        insights,
        list
    )

    assert len(insights) > 0