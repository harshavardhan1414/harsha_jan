# Demonstrates behavior of immutable default parameters

def count_message(msg, count=0):
    count += 1    
    print(f"Message: {msg}  Current Count: {count}") 
    return count
count_message("Hi")
count_message("Hello")
count_message("i love ML")