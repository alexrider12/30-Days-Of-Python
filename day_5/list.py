# 1
emptyList = []
# 2
fiveItemsList = ['1','2','3','4','5','6']
print(fiveItemsList)
# 3
print("Nr.3",len(fiveItemsList))
# 4
print("Nr.4",fiveItemsList[0],fiveItemsList[len(fiveItemsList)//2-1],fiveItemsList[-1])
# 5
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 6
print("Nr.6",len(it_companies), it_companies)
# 7
print("Nr.7",it_companies[0],it_companies[len(it_companies)//2-1],it_companies[-1])
# 8
it_companies[0] = 'Vector'
print("Nr.8", it_companies)
# 9
it_companies.append('new One')
print("Nr.9",it_companies)
# 10
it_companies.insert(len(it_companies)//2-1, 'secound')
print("Nr.10",it_companies)
# 11
it_companies[0] = it_companies[0].upper()
print("Nr.11",it_companies)
# 12
print("Nr.12","#; ".join(it_companies))
# 13
del it_companies[0:3]
print("Nr.13", it_companies)
# 14
del it_companies[len(it_companies)-3:len(it_companies)]
print("Nr.14", it_companies)
# 15
del it_companies[0:len(it_companies)]
print("Nr.15",it_companies)

print("----Level2---")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort(reverse=False)
print(ages)

ages.insert(0, ages[0])
ages.insert(-1, ages[-1])
print(ages)
print("Median:",ages[len(ages)//2-1])

allAges = 0
for _ in ages:
    allAges += _
averageAge = allAges/len(ages)
spanAge = max(ages) - min(ages)
print(f"span {spanAge}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

number = int()
print("mid" ,countries[len(countries)//2])
firstPart = countries[0:len(countries)//2]
lastPart = countries[len(countries)//2:len(countries)]
print("full",len(countries))
print("fist",len(firstPart))
print("last", len(lastPart))

item1, item2, item3, *rest = countries
print(item1)