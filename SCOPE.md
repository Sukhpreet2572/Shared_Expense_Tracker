# SCOPE.md

# Shared Expenses App

## Project Overview

The Shared Expenses App is designed to import and manage shared expenses for a group of flatmates. The application supports changing group membership, multiple expense split methods, settlement tracking, anomaly detection, and balance calculation.

The primary objective is to safely import messy financial data from the provided CSV while maintaining auditability and preventing silent data corruption.

---

# Functional Scope

## User Management

Supported Features:

- User Registration
- User Login
- User Authentication
- Profile Management

---

## Group Management

Supported Features:

- Create Groups
- Add Members
- Remove Members
- Track Membership History

Membership is time-aware.

Each membership record contains:

- Join Date
- Leave Date

This allows accurate balance calculations when members join or leave during the lifecycle of the group.

---

## Expense Management

Supported Expense Types:

### Equal Split

Example:

Expense Amount = ₹4000

Participants = 4

Each participant owes ₹1000.

---

### Unequal Split

Example:

Participant A = ₹700

Participant B = ₹400

Participant C = ₹400

---

### Percentage Split

Example:

Aisha = 30%

Rohan = 30%

Priya = 20%

Meera = 20%

Total must equal 100%.

---

### Share-Based Split

Example:

Aisha = 1 share

Rohan = 2 shares

Priya = 1 share

Total amount distributed proportionally.

---

# Supported Transaction Categories

## Expense

Normal shared spending.

Examples:

- Rent
- Groceries
- Electricity
- Internet
- Maid Salary

---

## Settlement

Repayment between members.

Example:

- Rohan paid Aisha back

Settlements reduce outstanding balances.

---

## Refund

Money returned after a previous expense.

Example:

- Parasailing Refund

Refunds may contain negative values.

---

## Deposit

Non-consumption payments.

Example:

- Security Deposit
- Sam Deposit Share

Deposits are tracked separately from shared expenses.

---

# CSV Import Scope

The system imports the CSV exactly as provided.

Manual editing before import is not required.

Import Process:

1. Upload CSV
2. Parse Data
3. Detect Anomalies
4. Generate Import Report
5. User Reviews Issues
6. Import Approved Records
7. Store Audit Trail

---

# Anomalies Detected

## A1 - Duplicate Expense

Detection:

- Same date
- Same amount
- Same payer
- Same participants

Action:

Flag for review.

---

## A2 - Member Alias

Examples:

- Priya
- priya
- Priya S

Action:

Suggest merge.

---

## A3 - Missing Payer

Detection:

paid_by field empty.

Action:

Mark Pending Review.

---

## A4 - Settlement Recorded As Expense

Detection:

Description or notes indicate repayment.

Action:

Convert to Settlement.

---

## A5 - Missing Currency

Detection:

Currency field empty.

Action:

Flag and suggest likely currency.

---

## A6 - Ambiguous Date

Examples:

04/05/2026

Action:

Require user confirmation.

---

## A7 - Invalid Percentage Split

Detection:

Percentage total ≠ 100%.

Action:

Block automatic calculation.

---

## A8 - Invalid Unequal Split

Detection:

Split amounts ≠ Expense Amount.

Action:

Flag for review.

---

## A9 - Conflicting Split Definition

Example:

split_type = equal

split_details = share based

Action:

Flag for review.

---

## A10 - Negative Amount

Detection:

Amount < 0

Action:

Treat as Refund.

---

## A11 - Zero Amount Transaction

Detection:

Amount = 0

Action:

Import and flag.

---

## A12 - Inactive Member Included

Detection:

Expense date outside member's active period.

Action:

Suggest participant removal.

---

## A13 - Guest Participant

Detection:

Participant not part of group membership.

Action:

Create Guest Participant.

---

# Membership Rules

## Permanent Members

- Aisha
- Rohan
- Priya

---

## Former Members

- Meera

Leave Date:

31 March 2026

---

## New Members

- Sam

Join Date:

08 April 2026

---

## Temporary Participants

- Dev

Trip-only participant.

---

## Guests

- Kabir

Expense-specific participant.

---

# Import Report Requirements

Every import must generate a report containing:

- Total Rows Processed
- Successful Imports
- Failed Imports
- Anomalies Detected
- Actions Taken

Example:

Row 22

Issue:
Missing Payer

Action:
Marked Pending Review

---

# Non-Functional Requirements

## Auditability

Every anomaly must be recorded.

---

## Data Preservation

No financial record is silently deleted.

---

## Traceability

Every transformation must be logged.

---

## Extensibility

New split types and transaction categories can be added without redesigning the system.

---

# Out of Scope

The following are intentionally excluded:

- Multi-currency live exchange rate APIs
- Multiple groups per expense
- Recurring expense automation
- Mobile applications
- Real-time notifications
- OCR receipt scanning

These features are not required for the assignment.
