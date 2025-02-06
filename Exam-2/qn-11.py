class Logger:
    def log(self, message, level="info"):
        if level == "error":
            print(f"[ERROR] {message}")
        elif level == "warning":
            print(f"[WARNING] {message}")
        else:
            print(f"[INFO] {message}")

logger = Logger()

logger.log("This is an error message", "error")

logger.log("This is a warning message", "warning")

logger.log("This is an info message")
