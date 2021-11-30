# Divide packages into three equal groups by weight.
# Group 1 needs to have the smallest number of packages possible
# Once the smallest number of packages is determined then first needs to have
# the lowest possible qe

from typing import DefaultDict


packages = [
  1,
  3,
  5,
  11,
  13,
  17,
  19,
  23,
  29,
  31,
  41,
  43,
  47,
  53,
  59,
  61,
  67,
  71,
  73,
  79,
  83,
  89,
  97,
  101,
  103,
  107,
  109,
  113
]

target_weight = sum(packages) / 4
print(target_weight)

results = DefaultDict(list)

def add_package(last_package_added: int, number_of_packages: int, current_weight: int, current_qe: int):
  if current_weight == target_weight:
    results[number_of_packages].append(current_qe)
  elif current_weight < target_weight:
    for package in packages:
      if package > last_package_added:
        add_package(package, number_of_packages+1, current_weight+package, current_qe*package)

for package in packages:
  add_package(package, 1, package, package)

smallest_number_of_packages = min(results.keys())
smallest_qe = min(results[smallest_number_of_packages])


print(smallest_qe)
