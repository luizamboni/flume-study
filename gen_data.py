#!/usr/bin/env python

from random import shuffle
from random import randint
import datetime
import sys
import time


n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
interval = int(sys.argv[2]) if len(sys.argv) > 2 else 1

def gen_value(value, n, result = []):
  local_result = list(result)
  local_result.append((value, 1))

  n = n - 1

  if (n == 0):
    return local_result
  else:
    return gen_value(value, n, local_result)

def gen_sequence(initial = 0, increment = 1):

  n = initial
  while(True):
    yield n
    n = n + increment

def gen_value(event_conf):
  event_ranges = gen_set(event_conf)
  events_domain = map(lambda a: a[2], event_ranges)
  event = randint(0, max(events_domain))

  for event_range in event_ranges:
    if (event >= event_range[1] and event <= event_range[2]):
      return event_range[0]

def gen_set(percentis):

  state = { 
    "current_point" : 0,
    "prev": 0
  }

  def gen_slice(item):

    label = item[0]
    end = item[1]

    state["current_point"]  = state["current_point"] + end
    prev_value = state["prev"]
    item = (label, prev_value, state["current_point"] )
    state["prev"] = state["current_point"] + 1
    return item

  events_domain = map(lambda a: a[1], percentis)
  event = randint(0, sum(events_domain))

  # achar qual item de lista o evento se encontra
  return map(gen_slice, percentis)


def sample(n, conf):

  id_sequence = gen_sequence()
  now = datetime.datetime.now()

  for idx in range(n):
    age = randint(25, 55)

    print({
      "sample_n": idx,
      "id": next(id_sequence),
      "gender" : gen_value(conf["gender"]),
      "name": gen_value(conf["first_names"]) + " " + gen_value(conf["last_names"]),
      "position": gen_value(conf["positions"]),
      "age": age,
      "bithdate": datetime.date(now.year - age, 1, 1).isoformat()
    })

genders = [
  ("male", 40),
  ("female", 55),
  ("trans-female", 5)
]

first_names = [
  ("luiz", 10), 
  ("paulo", 30),
  ("joao", 30),
  ("alexandre", 30),
]

last_names = [
  ("assis", 10), 
  ("zamboni", 30),
  ("fernandes", 30),
  ("raposo", 30),
]


positions = [
  ("admin", 10), 
  ("developer", 65),
  ("engeneer", 5),
  ("architect", 20),
]

while (True):

  sample(n, {
    "gender" : genders,
    "positions": positions,
    "last_names": last_names,
    "first_names": first_names,
  })

  time.sleep(interval)
