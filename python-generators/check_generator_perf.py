import memory_profiler as mem_profile
import random
import time

names = ['Dravid', 'Ponting', 'Kallis', 'Anderson']
country = ['India', 'Australia', 'South Africa', 'England']

print('Memory (Before): {} Mb'.format(mem_profile.memory_usage()))

def create_list(num_people):
    result = []
    for pl in range(num_people):
        person = {
            'id': pl,
            'name': random.choice(names),
            'country': random.choice(country)
        }
        result.append(person)
    return result

def create_gen(num_people):
    for pl in range(num_people):
        person = {
            'id': pl,
            'name': random.choice(names),
            'country': random.choice(country)
        }
        yield person

# time_a = time.perf_counter()
# people = create_list(10000)
# time_b = time.perf_counter()

time_a = time.perf_counter()
people = create_gen(10000)
time_b = time.perf_counter()

print('Memory (After): {} Mb'.format(mem_profile.memory_usage()))
print('Executing took {} seconds'.format(time_b-time_a))