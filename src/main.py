from fasthtml.common import *

app = FastHTML(hdrs=Link(rel="stylesheet", href="app.css", type="text/css"))


@app.route("/{fname:path}.{ext:static}")
def serve_files(fname:str, ext:str):
  "production fileserver with caching"
  @flexicache(mtime_policy("./public/"))
  def f(fname, ext):
    return FileResponse(f'public/{fname}.{ext}')
  return f(fname, ext)

serve(reload=True)

@app.route("/")
def mainpage():
  return(
    Title("Leaderboard"),
    Head(
    ),
    Body(
      Div(),
      Div(
        P("Hi!"),
        ),
      cls='text-base text-white bg-[#0f0f23]'
    )
  )

