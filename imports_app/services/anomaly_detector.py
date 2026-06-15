def is_duplicate(self, current_row, all_rows):

    current_description = (
        current_row["description"]
        .lower()
        .replace("-", "")
        .strip()
    )

    for row in all_rows:

        if row == current_row:
            continue

        description = (
            row["description"]
            .lower()
            .replace("-", "")
            .strip()
        )

        if (
            row["date"] == current_row["date"]
            and row["paid_by"] == current_row["paid_by"]
            and row["amount"] == current_row["amount"]
            and description == current_description
        ):
            return True

    return False