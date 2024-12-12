import os, httpx

from fasthtml.common import *
from fastcore.utils import *

app = FastHTML(hdrs=Link(rel="stylesheet", href="../app.css", type="text/css"))

@app.route("/{fname:path}.{ext:static}")
def serve_files(fname:str, ext:str):
  "production fileserver with caching"
  @flexicache(mtime_policy("./public/"))
  def f(fname, ext):
    return FileResponse(f'public/{fname}.{ext}')

  return f(fname, ext)

@app.route("/")
def mainpage():
  return (
    Title("2024 Leaderboard"),
    Head(
      Link(rel='preconnect', href='https://fonts.googleapis.com'),
      Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
      Link(href='https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,200..900;1,200..900&display=swap', rel='stylesheet'),
      StyleX("css/hide_scrollbar.css"),
    ),
    Body(
      intro(),
      Div(cls=''),
      Div(
        leaderboard_2024(),
        ),
      Div(cls=''),
      cls='font-scp text-base text-whi bg-[#0f0f23] mt-4 pt-4',
    )
  )

@app.route("/day/{slug}")
def day(slug: str):
  day = int(slug)

  return (
    Title(f"Day {day} Leaderboard"),
    Head(
      Link(rel='preconnect', href='https://fonts.googleapis.com'),
      Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
      Link(href='https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,200..900;1,200..900&display=swap', rel='stylesheet'),
      StyleX("css/hide_scrollbar.css"),
    ),
    Body(
      day_intro(day),
      Div(cls=''),
      Div(
        daily_leaderboard(day),
        ),
      Div(cls=''),
      cls='font-scp text-base text-whi bg-[#0f0f23] mt-4 pt-4'
    )
  )

def intro():
  return (
    Div(
      #P('This is an alternate', cls='inline'),
      #P('Solveit', cls='inline text-yel'),
      #P('Leaderboard', cls='inline text-yel'),
      #P(' for', cls='inline'),
      #P('Advent of Code 2024', cls='text-white tpx-1 rounded inline'),
      #P('; it is different from the', cls='inline'),
      #A('[Global Leaderboard]', href='https://adventofcode.com/2024/leaderboard', cls='text-gre hover:text-lgre inline'),
      #Br(),
      #Br(),
      #Div(
      #P("Scoring:", cls='inline text-white'),
      #P("First solve gets 100 points, second 99 etc.. down to 1 point per star, awarded separately for parts 1 and 2.", cls='inline'),
      #),
      #Br(),
      Div(
        Div(

        A(
          P("Y(",cls='inline text-gre group-hover:text-lgre'), P('2024', cls='inline text-lgre group-hover:text-lgre'), P(')',cls='inline text-gre group-hover:text-lgre'),
          href='/', cls='inline text-gre hover:text-lgre text-bold group text-bold'
          ),

          cls='inline hover:text-lgre'
        ),
        navigation_by_day(),
        cls='inline'
      ),
    cls='w-1/2 max-w-2xl mx-auto text-whi leading-normal p-16 px-4'
    ),
)

def day_intro(day=1):
  return (
    Div(
      #P('This is an alternate', cls='inline'),
      #P('Solveit', cls='inline text-yel'),
      #P('Leaderboard', cls='inline text-yel'),
      #P(' for', cls='inline'),
      #P('Advent of Code 2024', cls='text-white tpx-1 rounded inline'),
      #P('; it is different from the', cls='inline'),
      #A('[Global Leaderboard]', href='https://adventofcode.com/2024/leaderboard', cls='text-gre hover:text-lgre inline'),
      #Br(),
      #Br(),
      #Div(
      #P("Scoring:", cls='inline text-white'),
      #P("The daily ranking on this leaderboard is based entirely on the time delta between solving the 1st and 2nd problem.", cls='inline'),
      #),
      #Br(),
      Div(
        A(
          P("Y(",cls='inline text-gre group-hover:text-lgre'), P('2024', cls='inline text-lgre group-hover:text-lgre'), P(')',cls='inline text-gre group-hover:text-lgre'),
          href='/', cls='inline text-gre hover:text-lgre text-bold group text-bold'
          ),
        # P(" ",cls='inline'),
        navigation_by_day(day),
        cls='inline'
      ),
    cls='w-1/2 max-w-2xl mx-auto text-whi leading-normal p-16 px-4'
    ),
)

def navigation_by_day(dsel=0):
  return (
    Div(
    # TODO: make this dynamic don't hardcode this. Can just get days from the data.
      A('[1]', href='/day/1', cls=f'{"text-whi" if dsel == 1 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[2]', href='/day/2', cls=f'{"text-whi" if dsel == 2 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[3]', href='/day/3', cls=f'{"text-whi" if dsel == 3 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[4]', href='/day/4', cls=f'{"text-whi" if dsel == 4 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[5]', href='/day/5', cls=f'{"text-whi" if dsel == 5 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[6]', href='/day/6', cls=f'{"text-whi" if dsel == 6 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[7]', href='/day/7', cls=f'{"text-whi" if dsel == 7 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[8]', href='/day/8', cls=f'{"text-whi" if dsel == 8 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[9]', href='/day/9', cls=f'{"text-whi" if dsel == 9 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[10]', href='/day/10', cls=f'{"text-whi" if dsel == 10 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[11]', href='/day/11', cls=f'{"text-whi" if dsel == 11 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[12]', href='/day/12', cls=f'{"text-whi" if dsel == 12 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      *future_days(),
    cls='inline text-base',
    )
  )

# ***** TODO: clean up this messy code below.
# # testing

# GOOD
def duration(t): return AttrDict(name=t.name, duration=t.p2-t.p1)
def future_days(): return [ Div(P(f'[{i}]', cls="inline text-grey"), P(" ",cls='inline'),cls='inline') for i in range(13, 26) ]
def conv_secs(s): return f"{s//3600}:{(s%3600)//60:02d}:{s%60:02d}" if s>=3600 else f"{s//60}:{s%60:02d}" if s>=60 else str(s)

# GOOD
@flexicache(time_policy(1000))
def fetch_data():
  url = 'https://adventofcode.com/2024/leaderboard/private/view/3297706.json'
  r = httpx.get(url, cookies={'session': os.environ['AOC_SESSION']})
  return r.json()

# GOOD
def part2_time(member, daynum):
    days = member.get('completion_day_level', {})
    day = days.get(str(daynum), {})
    if '2' in day: return AttrDict(name = member['name'], p1 = day['1']['get_star_ts'], p2 = day['2']['get_star_ts'])

# GOOD
@flexicache(time_policy(1000))
def daily_leaderboard(day=1):
  d = fetch_data()
  times = L(d['members'].values()).map(part2_time, daynum=day).filter()
  leaderboard = times.map(duration).sorted('duration')
  board = [ Div(P(f"{i+1})", cls='w-6 text-left pr-2 text-grey'), P(t.name or '(anonymous user)', cls='flex-grow text-grey hover:text-whi'), P(f"{conv_secs(t.duration)}",
            cls='text-right text-whi'), cls='flex items-center space-x-4 py-1') for i, t in enumerate(leaderboard) ]
  return (
    Div(
      *board,
      cls='w-full max-w-md mx-auto'
    )
  )

# TODO: REFACTOR ME
@flexicache(time_policy(1000))
def get_completion_times(member, daynum):
  days = member.get('completion_day_level', {})
  day = days.get(str(daynum), {})

  p1_time = day.get('1', {}).get('get_star_ts', None) if '1' in day else None
  p2_time = day.get('2', {}).get('get_star_ts', None) if '2' in day else None
  p3_time = day.get('3', {}).get('get_star_ts', None) if '3' in day else None
  p4_time = day.get('4', {}).get('get_star_ts', None) if '4' in day else None
  p5_time = day.get('5', {}).get('get_star_ts', None) if '5' in day else None
  p6_time = day.get('6', {}).get('get_star_ts', None) if '6' in day else None
  p7_time = day.get('7', {}).get('get_star_ts', None) if '7' in day else None
  p8_time = day.get('8', {}).get('get_star_ts', None) if '8' in day else None
  p9_time = day.get('9', {}).get('get_star_ts', None) if '9' in day else None
  p10_time = day.get('10', {}).get('get_star_ts', None) if '10' in day else None
  p11_time = day.get('11', {}).get('get_star_ts', None) if '11' in day else None
  p12_time = day.get('12', {}).get('get_star_ts', None) if '12' in day else None

  if p1_time is not None or p2_time is not None:
    return AttrDict(name=member['name'], p1=p1_time, p2=p2_time, p3=p3_time, p4=p4_time, p5=p5_time, p6=p6_time, p7=p7_time, p8=p8_time, p9=p9_time, p10=p10_time, p11=p11_time, p12=p12_time)

# TODO: REFACTOR ME
@flexicache()
def leaderboard_2024():
  d = fetch_data()
  days = set()
  for member in d['members'].values():
    days.update(member.get('completion_day_level', {}).keys())

  total_points = {}
  for day in days:
    times = L(d['members'].values()).map(get_completion_times, daynum=int(day)).filter()
    day_leaderboard = calculate_points(times)
    for entry in day_leaderboard: total_points[entry.name] = total_points.get(entry.name, 0) + entry.points

  final_leaderboard = L(total_points.items()).map(lambda x: AttrDict(name=x[0], points=x[1])).sorted('points', reverse=True)
  board = [ Div(P(f"{i})", cls='w-6 text-left pr-2 text-grey'), P(t.name, cls='flex-grow text-grey hover:text-whi'), P(f"{t.points}", cls='text-right text-whi'), cls='flex items-center space-x-4 py-1') if t.name else None for i, t in enumerate(final_leaderboard) ]

  return (
    Div(
      *board,
      cls='w-full max-w-md mx-auto'
    )
  )

# TODO: REFACTOR ME
def calculate_points(times):
    p1_sorted = sorted((t for t in times if t.p1 is not None), key=lambda x: x.p1)
    p2_sorted = sorted((t for t in times if t.p2 is not None), key=lambda x: x.p2)
    p3_sorted = sorted((t for t in times if t.p3 is not None), key=lambda x: x.p3)
    p4_sorted = sorted((t for t in times if t.p4 is not None), key=lambda x: x.p4)
    p5_sorted = sorted((t for t in times if t.p5 is not None), key=lambda x: x.p5)
    p6_sorted = sorted((t for t in times if t.p6 is not None), key=lambda x: x.p6)
    p7_sorted = sorted((t for t in times if t.p7 is not None), key=lambda x: x.p7)
    p8_sorted = sorted((t for t in times if t.p8 is not None), key=lambda x: x.p8)
    p9_sorted = sorted((t for t in times if t.p9 is not None), key=lambda x: x.p9)
    p10_sorted = sorted((t for t in times if t.p10 is not None), key=lambda x: x.p10)
    p11_sorted = sorted((t for t in times if t.p11 is not None), key=lambda x: x.p11)
    p12_sorted = sorted((t for t in times if t.p12 is not None), key=lambda x: x.p12)

    points = {}
    for i, t in enumerate(p1_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p2_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p3_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p4_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p5_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p6_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p7_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p8_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p9_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p10_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p11_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)
    for i, t in enumerate(p12_sorted): points[t.name] = points.get(t.name, 0) + max(100 - i, 1)

    leaderboard = L(points.items()).map(lambda x: AttrDict(name=x[0], points=x[1])).sorted('points', reverse=True)
    return leaderboard


# ***** FOR DEBUGING AND DEVELOPMENT
serve(reload=False)
