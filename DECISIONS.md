# DECISIONS.md

## Project: Shared Expenses App

This document records significant product and engineering decisions made during the development of the Shared Expenses App. Each decision includes the problem identified, alternative approaches considered, and the rationale behind the final choice.

---

# Decision 1: Duplicate Expense Handling

## Problem

The CSV contains expenses that appear to represent the same transaction with minor description variations.

Example:

- Dinner at Marina Bite
- dinner - marina bites

Both have identical date, payer, amount, and participants.

## Options Considered

### Option A

Automatically delete one record.

### Option B

Keep both records.

### Option C (Chosen)

Flag as a Potential Duplicate and require user review.

## Reason

Financial applications should not silently delete transaction data. The user must approve any removal or merge operation.

---

# Decision 2: Member Alias Detection

## Problem

The same person appears under multiple names.

Examples:

- Priya
- priya
- Priya S

## Options Considered

### Option A

Automatically merge names.

### Option B

Treat all names as separate people.

### Option C (Chosen)

Flag as Possible Member Alias and suggest a merge.

## Reason

Automatic identity merging may incorrectly combine different people. User confirmation is required.

---

# Decision 3: Missing Payer Information

## Problem

Some expenses have no value in the paid_by field.

Example:

- House cleaning supplies

## Chosen Solution

Import the expense but mark it as Pending Review.

## Reason

The transaction may still be valid. Excluding it entirely would result in data loss.

---

# Decision 4: Settlement Detection

## Problem

Some rows represent repayments rather than actual expenses.

Example:

- Rohan paid Aisha back

## Chosen Solution

Convert these rows into Settlement transactions.

## Reason

Repayments affect balances but do not represent spending.

---

# Decision 5: Currency Preservation

## Problem

The dataset contains both INR and USD transactions.

## Chosen Solution

Store:

- Original Amount
- Original Currency
- Conversion Rate
- Converted Amount

## Reason

Original financial records should never be overwritten.

---

# Decision 6: Membership Timeline

## Problem

Group membership changes over time.

Examples:

- Meera leaves at the end of March
- Sam joins in April
- Dev participates only during the Goa trip

## Chosen Solution

Track membership periods using:

- joined_at
- left_at

## Reason

Expenses should only affect members active at the time the expense occurred.

---

# Decision 7: Guest Participants

## Problem

Some expenses involve people who are not permanent members.

Example:

- Kabir

## Chosen Solution

Create Guest Participants instead of adding them as permanent group members.

## Reason

Guests should not appear in future balance calculations unrelated to them.

---

# Decision 8: Negative Amount Handling

## Problem

Negative amounts appear in the dataset.

Example:

- Parasailing refund (-30 USD)

## Chosen Solution

Treat negative values as Refund Transactions.

## Reason

Refunds are legitimate financial events and should not be rejected.

---

# Decision 9: Ambiguous Date Formats

## Problem

The CSV contains multiple date formats.

Examples:

- 2026-02-01
- 01/03/2026
- Mar 14
- 04/05/2026

## Chosen Solution

Detect ambiguous dates and require review.

## Reason

Incorrect date interpretation changes balance calculations.

---

# Decision 10: Invalid Split Definitions

## Problem

Some rows contain inconsistent split information.

Examples:

- Percentages that may not total 100%
- Unequal amounts that do not add up correctly
- Equal split type with share-based details

## Chosen Solution

Flag these transactions and prevent automatic balance calculation.

## Reason

Financial calculations should only occur on validated split information.

---

# Decision 11: Security Deposit Transactions

## Problem

Some payments represent deposits rather than expenses.

Example:

- Sam deposit share

## Chosen Solution

Store as Deposit transactions.

## Reason

Deposits do not represent shared consumption and should not affect expense balances.

---

# Decision 12: Zero Value Transactions

## Problem

Some rows contain an amount of zero.

Example:

- Dinner order Swiggy (0 INR)

## Chosen Solution

Import and flag for review.

## Reason

The transaction may represent a correction or cancellation and should remain auditable.

---

# Decision 13: Inactive Member Participation

## Problem

Expenses may include members after they have left the group.

Example:

- Meera appears in April expenses despite moving out in March.

## Chosen Solution

Flag the expense and suggest removing inactive members.

## Reason

Only active members should share expenses occurring during their membership period.

---

# Decision 14: Data Preservation First

## Guiding Principle

The application should never silently delete, merge, or modify financial records.

## Chosen Solution

Every anomaly must:

1. Be detected
2. Be shown in the Import Report
3. Record the action taken

## Reason

This aligns with auditability requirements and user trust expectations.
