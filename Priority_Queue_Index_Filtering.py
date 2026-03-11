tickets = ["Password Reset", "Bug Report", "Feature Request", "Account Locked", "Payment Issue", "General Query", "Refund Request"]

high_priority = 0

for index, ticket in enumerate(tickets):

    if index % 3 == 0:
        priority = "High priority"
        high_priority += 1
    elif index <= 2:
        priority = "Medium priority"
    else:
        priority = "Low priority"

    print(f"Ticket {index}: {ticket} - {priority}")
print("\nTotal High Priority Tickets:", high_priority)