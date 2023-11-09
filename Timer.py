import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        if self.start_time is not None:
            print("Timer is already running. Use stop() to stop the current timer.")
        else:
            self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            print("Timer is not running. Use start() to start a new timer.")
        else:
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            self.start_time = None
            print(f"Timer stopped. Elapsed time: {elapsed_time:.2f} seconds")