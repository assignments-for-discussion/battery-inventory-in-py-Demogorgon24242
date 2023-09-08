
def soh_calc(capacity):
  rated_capacity= 120.0
  soh_vals=[]
  for i in capacity:
    if i<0:
      continue
    soh=  100 * (i/ rated_capacity)
    soh_vals.append(soh)
  return soh_vals



def count_batteries_by_health(present_capacities):
  soh = soh_calc(present_capacities)
  health=0
  exchange=0
  fail=0
  for i in soh:
    if i>80.00 :
      health+=1
    elif i<=80.00 and i>=65.00:
      exchange+=1
    else:
      fail+=1
  return {
    "healthy": health,
    "exchange": exchange,
    "failed": fail
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77,-100]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
