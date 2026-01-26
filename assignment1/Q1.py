def count_message(msg, count=0):
    """
    This function accepts a message and a default count.
    Since integers are immutable, the count resets on every function call.
    """
    count += 1
    print(f"Message: {msg}, Count: {count}")
    return count
count_message("heya")
count_message("hello again")
count_message("third call")
