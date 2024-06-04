try:
    import requests
    from bs4 import BeautifulSoup
    print("Modules imported successfully!")
except ImportError as e:
    print(f"Error importing modules: {e}")