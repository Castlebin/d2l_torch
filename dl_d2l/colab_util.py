
# Utility function to check if the code is running in Google Colab
def is_colab():
    try:
        import google.colab  # noqa: F401
        return True
    except ImportError:
        return False


# ==================== Main Program ====================
if __name__ == "__main__":
    if is_colab():
        print("Running in Google Colab")
    else:
        print("Not running in Google Colab")

