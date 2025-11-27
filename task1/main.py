import queue
import time
import random

# Create a request queue
request_queue = queue.Queue()

# Counter for unique request IDs
request_id = 1

def generate_request():
    """Generate a new request and add it to the queue"""
    global request_id
    # Create a request as a dictionary with a unique ID and some data
    request = {"id": request_id, "data": f"Request data {request_id}"}
    request_queue.put(request)  # Add the request to the queue
    print(f"Request created: {request}")
    request_id += 1

def process_request():
    """Process a request from the queue if available"""
    if not request_queue.empty():
        request = request_queue.get()  # Remove the request from the queue
        print(f"Processing request: {request}")
        # Simulate processing time
        time.sleep(random.uniform(0.5, 1.5))
    else:
        print("Queue is empty, no requests to process.")

def main():
    """Main program loop"""
    try:
        while True:
            # Generate a random number of requests (1-3) per cycle
            for _ in range(random.randint(1, 3)):
                generate_request()
            # Process one request per cycle
            process_request()
            # Delay for clarity
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
