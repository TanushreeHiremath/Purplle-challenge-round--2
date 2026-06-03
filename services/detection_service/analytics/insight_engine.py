def generate_ai_insights(
    funnel_data
):

    insights = []

    entered = funnel_data.get(
        "entered",
        0
    )

    browsed = funnel_data.get(
        "browsed",
        0
    )

    queued = funnel_data.get(
        "queued",
        0
    )

    purchased = funnel_data.get(
        "purchased",
        0
    )

    # ====================================
    # CONVERSION ANALYSIS
    # ====================================

    if entered > 0:

        conversion_rate = (
            purchased / entered
        ) * 100

        if conversion_rate < 30:

            insights.append(
                "Low conversion rate detected. Customers may require better purchase assistance."
            )

        elif conversion_rate < 60:

            insights.append(
                "Moderate conversion performance observed."
            )

        else:

            insights.append(
                "Strong conversion rate observed across store visitors."
            )

    # ====================================
    # QUEUE ANALYSIS
    # ====================================

    if queued > 5:

        insights.append(
            "Billing queue congestion increasing during current session."
        )

    elif queued > 0:

        insights.append(
            "Billing queue operating within manageable levels."
        )

    # ====================================
    # BROWSING ANALYSIS
    # ====================================

    if entered > 0 and browsed > entered * 0.7:

        insights.append(
            "High customer engagement detected in browsing zones."
        )

    # ====================================
    # PURCHASE ANALYSIS
    # ====================================

    if purchased > 0:

        insights.append(
            "Successful purchase activity detected from active visitors."
        )

    # ====================================
    # FALLBACK
    # ====================================

    if len(insights) == 0:

        insights.append(
            "Store activity currently stable with limited operational anomalies."
        )

    return insights