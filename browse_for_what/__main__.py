if __name__ == "__main__":
    import os
    import browse_for_what.browseapp as app
    app.start(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.json")))
