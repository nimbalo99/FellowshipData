
import random
from faker import Faker
import csv
import itertools

fake = Faker()


personality_types = [
    "ISTJ - Inspector",
    "ISFJ - Protector",
    "INFJ - Counselor",
    "INTJ - Mastermind",
    "ISTP - Craftsman",
    "ISFP - Composer",
    "INFP - Healer",
    "INTP - Architect",
    "ESTP - Dynamo",
    "ESFP - Performer",
    "ENFP - Champion",
    "ENTP - Visionary",
    "ESTJ - Supervisor",
    "ESFJ - Provider",
    "ENFJ - Teacher",
    "ENTJ - Commander"
]

languages = [
    "Mandarin Chinese",
    "Spanish",
    "English",
    "Hindi",
    "Arabic",
    "Bengali",
    "Portuguese",
    "Russian",
    "Japanese",
    "Punjabi",
    "German",
    "Javanese",
    "Wu Chinese",
    "Malay",
    "Telugu",
    "Vietnamese",
    "Korean",
    "French",
    "Marathi",
    "Tamil"
]

countries = [
    'China',
    'India',
    'United States',
    'Indonesia',
    'Pakistan',
    'Brazil',
    'Nigeria',
    'Bangladesh',
    'Russia',
    'Mexico',
    'Japan',
    'Philippines',
    'Egypt',
    'Ethiopia',
    'Vietnam',
    'DR Congo',
    'Turkey',
    'Iran',
    'Germany',
    'Thailand',
    'United Kingdom',
    'France',
    'Tanzania',
    'Italy',
    'South Africa',
    'Myanmar',
    'South Korea',
    'Colombia',
    'Kenya',
    'Spain',
    'Ukraine',
    'Argentina',
    'Algeria',
    'Uganda',
    'Iraq',
    'Poland',
    'Canada',
    'Morocco',
    'Saudi Arabia',
    'Uzbekistan',
    'Peru',
    'Malaysia',
    'Angola',
    'Ghana',
    'Mozambique',
    'Yemen',
    'Nepal',
    'Venezuela',
    'Madagascar',
    'Cameroon',
    'North Korea',
    'Australia',
    'Taiwan',
    'Ivory Coast',
    'Niger',
    'Sri Lanka',
    'Burkina Faso',
    'Mali',
    'Romania',
    'Malawi',
    'Chile',
    'Kazakhstan',
    'Zambia',
    'Syria',
    'Netherlands',
    'Ecuador',
    'Guatemala',
    'Senegal',
    'Cambodia',
    'Chad',
    'Somalia',
    'Zimbabwe',
    'Guinea',
    'Rwanda',
    'Benin',
    'Tunisia',
    'Burundi',
    'Bolivia',
    'Belgium',
    'Haiti',
    'Cuba',
    'South Sudan',
    'Dominican Republic',
    'Czech Republic (Czechia)',
    'Greece',
    'Jordan',
    'Portugal',
    'Azerbaijan',
    'Sweden',
    'United Arab Emirates',
    'Honduras',
    'Hungary',
    'Tajikistan'
]


twitterAccounts = ["", "", "https://twitter.com/adventistchurch"]
instagramAccounts = ["", "https://www.instagram.com/adventistchurch"]
facebookAccounts = [
    "", "", "https://www.facebook.com/AdventistFrontierMissions"]
linkedInAccounts = [
    "", "", "https://www.linkedin.com/company/seventh-day-adventist-church/"]

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

# Generate random combinations of items with set lengths between 0 and 5


def combo(list, maxCombinations, scale, weightEmpty, weightOne, weightMultiple):
    result = []

    for i in range(scale*weightEmpty):
        result.append("")

    for i in range(scale*weightOne):
        result.append(random.choice(list))

    for r in range(maxCombinations):
        for i in range(scale*weightMultiple):
            result.append(','.join([item.strip()
                                    for item in random.sample(list, r)]))

    random.shuffle(result)

    return result


hobbySampleStrings = combo(hobbyLines, 10, 30, 10, 30, 20)

languageSampleStrings = combo(languages, 3, 10, 10, 30, 20)

countrySampleStrings = combo(countries, 3, 10, 10, 30, 10)

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
                         random.choice(countrySampleStrings).strip(),
                         random.choice(languageSampleStrings).strip(),
                         random.choice(relationshipLines).strip(),
                         random.choice(universityLines).strip(),
                         random.randint(1970, 2023),
                         random.choice(industryLines).strip(),
                        random.choice(jobLines).strip(),
                         random.choice(hobbySampleStrings).strip(),
                         random.choice(personality_types).strip(),
                         random.choice(twitterAccounts).strip(),
                         random.choice(instagramAccounts).strip(),
                         random.choice(facebookAccounts).strip(),
                         random.choice(linkedInAccounts).strip()])
