import sys

import streamlit as st
from streamlit.web import cli


def run_app():
    st.text("Hello World")


def main():
    if st.runtime.exists():
        run_app()
    else:
        sys.argv = ["streamlit", "run", __file__]
        sys.exit(cli.main())


if __name__ == "__main__":
    main()
