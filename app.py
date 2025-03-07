input_value = ""
total_time = 0

def process_time(input_time: str) -> float:
    """
    Process the input time and return the total time in hours.

    Args:
        input_time (str): The time to process. Format: HH.MM

    Returns:
        float: The total time in hours.
    """
    processed_time = 0

    try:
        time_parts = input_time.split(".")
        hours = int(time_parts[0])
        minutes = round(int(time_parts[1]) / 60, 2)
        
        processed_time = hours + minutes
    except Exception as e:
        print(f"Error processing time: {e}")
        return 0
    
    return processed_time

print("Enter the times and press enter after each one. Press . to finish.")
    
while input_value != ".":

    if input_value:
        total_time += process_time(input_value)
        print(f"  ={total_time}")

    input_value = input()
