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
      Link(rel='preconnect', href='https://fonts.googleapis.com'),
      Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
      Link(href='https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,200..900;1,200..900&display=swap', rel='stylesheet'),
    ),
    Body(
      Div(),
      Div(
        P("WHITE"),
        P("SOFT-WHITE", cls='text-gre'),
        P("GREEN", cls='text-[#009900]'),
        P("YELLOW", cls='text-[#ffff66]'),
        P("ORANGE", cls='text-[#886655]'),
        P("GREY", cls='text-[#666666]'),
        ),
      cls='font-scp text-base text-white bg-[#0f0f23]'
    )
  )

