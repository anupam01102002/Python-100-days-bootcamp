from game_data import data
from art import logo, vs
import random
print(logo)

n1 = random.randint(0, len(data))

print(f"Compare A: {data[n1]['name']}, a {data[n1]['description']}, from {data[n1]['country']}")
print(vs)

print(data[n1]['follower_count'])

n2 = random.randint(0, len(data))
while n2 == n1:
    n2 = random.randint(0, len(data))
    
print(f"Against B: {data[n2]['name']}, a {data[n2]['description']}, from {data[n2]['country']}")

print(data[n2]['follower_count'])

choice = input("who has more followers? Type 'A' or 'B': ")

if choice =='A':
    if data[n1]['follower_count'] > data[n2]['follower_count']:
        print("Won")
    else:
        print("lost")
if choice =='B':
    if data[n1]['follower_count'] > data[n2]['follower_count']:
        print("Won")
    else:
        print("lost")