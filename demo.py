import web

urls = (
  '/', 'index'
)

class index(object):
    def GET(self):
        return "hi mate"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
