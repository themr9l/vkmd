#!env/bin/python
# -*- coding: utf-8 -*-

import subprocess
from app import app


def main():
    app.run(debug=True, host="0.0.0.0")

if __name__ == '__main__':
    main()
