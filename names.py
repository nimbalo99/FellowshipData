
import random
from faker import Faker
import csv

fake = Faker()

years = range(1970, 2023)

# Open the file for reading
with open('PersonalityTypes.txt', 'r') as p:
    # Read all the lines into a list
    personalityLines = p.readlines()

with open('Industries.txt', 'r') as i:
    # Read all the lines into a list
    industryLines = i.readlines()

with open('Hobbies.txt', 'r') as h:
    # Read all the lines into a list
    hobbyLines = h.readlines()

with open('Universities.txt', 'r') as u:
    # Read all the lines into a list
    universityLines = u.readlines()

with open('RelationshipStatus.txt', 'r') as r:
    # Read all the lines into a list
    relationshipLines = r.readlines()

with open('Jobs.txt', 'r') as j:
    # Read all the lines into a list
    jobLines = j.readlines()

with open('ukChurches.txt', 'r') as c:
    # Read all the lines into a list
    churchLines = c.readlines()

# Generate 10 random full names

with open("names.csv", "a", newline="") as f:
    writer = csv.writer(f)

    for i in range(500):
        writer.writerow([fake.first_name() + " " + fake.last_name(),
                         random.choice(churchLines).strip(),
                         random.choice(jobLines).strip(),
                         random.choice(years),
                         random.choice(relationshipLines).strip(),
                         random.choice(universityLines).strip(),
                         random.choice(industryLines).strip(),
                         random.choice(hobbyLines).strip(),
                         random.choice(personalityLines).strip()])
