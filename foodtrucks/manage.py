from mysite import init_app

app = init_app('local')

if __name__ == '__main__':
    app.run()
