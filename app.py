from ClinicManagerApp import initTables, initAdmin, app


if __name__ == '__main__':
    initTables()
    initAdmin()
    app.run(port=5001)
