# While loop that continues while user has funds remaining

prompt the user to select an item by typing its name
check to make sure item exists in the "items" dictionary
    if not:
    - display an error message and us continue to prompt user again

    If found:
        - compare the cost of the selected item with the available funds

        if sufficient funds:
        - subtract price from the funds
        - print message that item is dispensed
        - show remaining balance

        if insufficient funds:
            - inform user of insufficient funds
            - ask if they wish to insert more money or cancel

            if user wants to add:
                - prompt for additional amount and update balance

                if not:
                    - use break to exit the loop

ask user if they want to make another purchase

    if yes, repeat loop
    if not, exit the loop 


    