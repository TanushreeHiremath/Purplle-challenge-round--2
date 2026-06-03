import pandas as pd


POS_DATA = pd.read_csv(
    "data/pos_transactions.csv"
)


POS_DATA["timestamp"] = pd.to_datetime(

    POS_DATA["order_date"]
    + " "
    + POS_DATA["order_time"],

    format="%d-%m-%Y %H:%M:%S"
)


def match_pos_transaction(
    event_time,
    time_window_seconds=30
):

    event_time = pd.to_datetime(
        event_time
    )

    for _, row in POS_DATA.iterrows():

        transaction_time = row["timestamp"]

        difference = abs(
            (
                transaction_time
                - event_time
            ).total_seconds()
        )

        if difference <= time_window_seconds:

            return {

                "matched": True,

                "transaction_id": str(
                    row["invoice_number"]
                ),

                "amount": float(
                    row["total_amount"]
                ),

                "store_id": row["store_id"],

                "salesperson": row[
                    "salesperson_name"
                ]
            }

    return {
        "matched": False
    }