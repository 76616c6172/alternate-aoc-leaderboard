from pathlib import Path

import os, httpx, json

from fasthtml.common import *
from fastcore.xtras import time
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
  return(
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
        default_leaderboard(),
        ),
      cls='font-scp text-base text-whi bg-[#0f0f23] mt-4 pt-4'
    )
  )

@app.route("/day/{slug}")
def day(slug: str):
  day = int(slug)

  return(
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
      cls='font-scp text-whi bg-[#0f0f23] mt-4 pt-4'
    )
  )

def intro():
  return(
    Div(
      P('This is an alternate', cls='inline'),
      P('Solveit', cls='inline text-yel'),
      P('Leaderboard', cls='inline text-yel'),
      P(' for', cls='inline'),
      P('Advent of Code 2024', cls='text-white tpx-1 rounded inline'),
      P('; it is different from the', cls='inline'),
      A('[Global Leaderboard]', href='https://adventofcode.com/2024/leaderboard', cls='text-gre hover:text-lgre inline'),
      Br(),
      Br(),
      Div(
      P("Scoring:", cls='inline text-white'),
      P("First solve gets 100 points, second 99 etc.. down to 1 point per star, awarded separately for parts 1 and 2.", cls='inline'),
      ),
      Br(),
      Div(
        A("2024", href='/', cls='inline text-whi text-bold'), P(" ",cls='inline'),
        navigation_by_day(),
        cls='inline'
      ),
    cls='w-1/2 max-w-2xl mx-auto text-whi leading-normal p-16 px-4'
    ),
)

def day_intro(day=1):
  return(
    Div(
      P('This is an alternate', cls='inline'),
      P('Solveit', cls='inline text-yel'),
      P('Leaderboard', cls='inline text-yel'),
      P(' for', cls='inline'),
      P('Advent of Code 2024', cls='text-white tpx-1 rounded inline'),
      P('; it is different from the', cls='inline'),
      A('[Global Leaderboard]', href='https://adventofcode.com/2024/leaderboard', cls='text-gre hover:text-lgre inline'),
      Br(),
      Br(),
      Div(
      P("Scoring:", cls='inline text-white'),
      P("The daily ranking on this leaderboard is based entirely on the time delta between solving the 1st and 2nd problem.", cls='inline'),
      ),
      Br(),
      Div(
        A("2024", href='/', cls='inline text-gre hover:text-lgre text-bold'), P(" ",cls='inline'),
        navigation_by_day(day),
        cls='inline'
      ),
    cls='w-1/2 max-w-2xl mx-auto text-whi leading-normal p-16 px-4'
    ),
)

def navigation_by_day(dsel=0):
  return(
      A('[1]', href='/day/1', cls=f'{"text-whi" if dsel == 1 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[2]', href='/day/2', cls=f'{"text-whi" if dsel == 2 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      A('[3]', href='/day/3', cls=f'{"text-whi" if dsel == 3 else "text-gre"} hover:text-lgre inline'), P(" ", cls='inline'),
      *future_days(),
  )


def part2_time(member, daynum):
    days = member.get('completion_day_level', {})
    day = days.get(str(daynum), {})
    if '2' in day: return AttrDict(name = member['name'], p1 = day['1']['get_star_ts'], p2 = day['2']['get_star_ts'])


def duration(t): return AttrDict(name=t.name, duration=t.p2-t.p1)
def future_days(): return [ Div(P(f'[{i}]', cls="inline text-grey"), P(" ",cls='inline'),cls='inline') for i in range(4, 25) ]
def conv_secs(s): return f"{s//3600}:{(s%3600)//60:02d}:{s%60:02d}" if s>=3600 else f"{s//60}:{s%60:02d}" if s>=60 else str(s)

@flexicache(time_policy(1000))
def fetch_data():
  url = 'https://adventofcode.com/2024/leaderboard/private/view/3297706.json'
  r = httpx.get(url, cookies={'session': os.environ['AOC_SESSION']})
  return r.json()


@flexicache(time_policy(1000))
def daily_leaderboard(day=1):
  d = fetch_data()
  times = L(d['members'].values()).map(part2_time, daynum=day).filter()
  leaderboard = times.map(duration).sorted('duration')
  board = [ Div(P(f"{i+1})", cls='w-6 text-left pr-2 text-grey'), P(t.name, cls='flex-grow text-whi'), P(f"{conv_secs(t.duration)}", cls='text-right text-white'), cls='flex items-center space-x-4 py-1') for i, t in enumerate(leaderboard) ]

  return (
    Div(
      *board,
      cls='w-full max-w-md mx-auto'
    )
  )

@flexicache(time_policy(1000))
def get_completion_times(member, daynum):
  days = member.get('completion_day_level', {})
  day = days.get(str(daynum), {})

  p1_time = day.get('1', {}).get('get_star_ts', None) if '1' in day else None
  p2_time = day.get('2', {}).get('get_star_ts', None) if '2' in day else None
  p3_time = day.get('3', {}).get('get_star_ts', None) if '3' in day else None

  if p1_time is not None or p2_time is not None:
    return AttrDict(name=member['name'], p1=p1_time, p2=p2_time, p3=p3_time)

@flexicache()
def default_leaderboard():
  d = fetch_data()
  days = set()
  for member in d['members'].values():
    days.update(member.get('completion_day_level', {}).keys())

  total_points = {}
  for day in days:
    times = L(d['members'].values()).map(get_completion_times, daynum=int(day)).filter()
    day_leaderboard = calculate_points(times)
    for entry in day_leaderboard:
      total_points[entry.name] = total_points.get(entry.name, 0) + entry.points

  final_leaderboard = L(total_points.items()).map(lambda x: AttrDict(name=x[0], points=x[1])).sorted('points', reverse=True)
  board = [ Div(P(f"{i+1})", cls='w-6 text-left pr-2 text-grey'), P(t.name, cls='flex-grow text-whi'), P(f"{t.points}", cls='text-right text-white'), cls='flex items-center space-x-4 py-1') for i, t in enumerate(final_leaderboard) ]

  return (
    Div(
      *board,
      cls='w-full max-w-md mx-auto'
    )
  )

def calculate_points(times):

    p1_sorted = sorted((t for t in times if t.p1 is not None), key=lambda x: x.p1)
    p2_sorted = sorted((t for t in times if t.p2 is not None), key=lambda x: x.p2)
    p3_sorted = sorted((t for t in times if t.p3 is not None), key=lambda x: x.p3)

    points = {}
    for i, t in enumerate(p1_sorted):
        points[t.name] = points.get(t.name, 0) + max(100 - i, 1)

    for i, t in enumerate(p2_sorted):
        points[t.name] = points.get(t.name, 0) + max(100 - i, 1)

    leaderboard = L(points.items()).map(lambda x: AttrDict(name=x[0], points=x[1])).sorted('points', reverse=True)
    return leaderboard


# ***** FOR DEBUGING AND DEVELOPMENT
#
serve(reload=False)
