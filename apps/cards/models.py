from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()



GENDER = (
    ('male', 'male'),
    ('female', 'female')
)

DEGREES = (
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
    ('PhD', 'PhD')
)

STATUS_OF_STUDIES = (
    ('In process', 'In process'),
    ('Finished', 'Finished')
)

WANTED_DEGREES = (
    # Technology & Engineering
    ('Software Engineering', 'Software Engineering'),
    ('Computer Science', 'Computer Science'),
    ('Information Technology', 'Information Technology'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Data Science', 'Data Science'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Machine Learning', 'Machine Learning'),
    ('Cloud Computing', 'Cloud Computing'),
    ('Network Engineering', 'Network Engineering'),
    ('Game Development', 'Game Development'),
    ('Mobile App Development', 'Mobile App Development'),
    ('Web Development', 'Web Development'),
    ('Computer Engineering', 'Computer Engineering'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Biomedical Engineering', 'Biomedical Engineering'),
    ('Robotics Engineering', 'Robotics Engineering'),
    ('Aerospace Engineering', 'Aerospace Engineering'),
    ('Automotive Engineering', 'Automotive Engineering'),
    ('Nanotechnology', 'Nanotechnology'),

    # Business & Finance
    ('Business Administration', 'Business Administration'),
    ('Entrepreneurship', 'Entrepreneurship'),
    ('Finance', 'Finance'),
    ('Accounting', 'Accounting'),
    ('Economics', 'Economics'),
    ('Marketing', 'Marketing'),
    ('Human Resource Management', 'Human Resource Management'),
    ('Supply Chain Management', 'Supply Chain Management'),
    ('Business Analytics', 'Business Analytics'),
    ('International Business', 'International Business'),
    ('Project Management', 'Project Management'),

    # Medicine & Health Sciences
    ('Medicine', 'Medicine'),
    ('Dentistry', 'Dentistry'),
    ('Pharmacy', 'Pharmacy'),
    ('Nursing', 'Nursing'),
    ('Physiotherapy', 'Physiotherapy'),
    ('Public Health', 'Public Health'),
    ('Veterinary Medicine', 'Veterinary Medicine'),
    ('Biotechnology', 'Biotechnology'),
    ('Psychology', 'Psychology'),
    ('Nutrition & Dietetics', 'Nutrition & Dietetics'),

    # Natural & Environmental Sciences
    ('Biology', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Physics', 'Physics'),
    ('Mathematics', 'Mathematics'),
    ('Environmental Science', 'Environmental Science'),
    ('Geology', 'Geology'),
    ('Meteorology', 'Meteorology'),
    ('Oceanography', 'Oceanography'),
    ('Astronomy', 'Astronomy'),

    # Social Sciences & Humanities
    ('Political Science', 'Political Science'),
    ('International Relations', 'International Relations'),
    ('Law', 'Law'),
    ('Criminal Justice', 'Criminal Justice'),
    ('Sociology', 'Sociology'),
    ('Anthropology', 'Anthropology'),
    ('History', 'History'),
    ('Philosophy', 'Philosophy'),
    ('Linguistics', 'Linguistics'),

    # Art, Media & Design
    ('Fine Arts', 'Fine Arts'),
    ('Graphic Design', 'Graphic Design'),
    ('Animation', 'Animation'),
    ('Film Production', 'Film Production'),
    ('Photography', 'Photography'),
    ('Music', 'Music'),
    ('Theater & Performing Arts', 'Theater & Performing Arts'),
    ('Fashion Design', 'Fashion Design'),
    ('Interior Design', 'Interior Design'),
    ('Architecture', 'Architecture'),

    # Aviation & Maritime
    ('Aviation Management', 'Aviation Management'),
    ('Pilot Training', 'Pilot Training'),
    ('Aeronautical Engineering', 'Aeronautical Engineering'),
    ('Marine Engineering', 'Marine Engineering'),
    ('Naval Architecture', 'Naval Architecture'),
    ('Logistics & Transportation', 'Logistics & Transportation'),

    # Education
    ('Primary Education', 'Primary Education'),
    ('Secondary Education', 'Secondary Education'),
    ('Special Education', 'Special Education'),
    ('Educational Leadership', 'Educational Leadership'),
    ('TESOL (Teaching English as a Second Language)', 'TESOL'),

    # Hospitality & Tourism
    ('Hospitality Management', 'Hospitality Management'),
    ('Tourism Management', 'Tourism Management'),
    ('Culinary Arts', 'Culinary Arts'),
    ('Event Management', 'Event Management'),

    # Sports & Recreation
    ('Sports Science', 'Sports Science'),
    ('Physical Education', 'Physical Education'),
    ('Sports Management', 'Sports Management'),

    # Miscellaneous
    ('Ethical Hacking', 'Ethical Hacking'),
    ('Game Design', 'Game Design'),
    ('Forensic Science', 'Forensic Science'),
    ('Archaeology', 'Archaeology'),
    ('Library & Information Science', 'Library & Information Science'),
)

WANTED_COUNTRIES = (
    ('United States', 'United States'),
    ('Canada', 'Canada'),
    ('United Kingdom', 'United Kingdom'),
    ('Australia', 'Australia'),
    ('Germany', 'Germany'),
    ('France', 'France'),
    ('Spain', 'Spain'),
    ('Italy', 'Italy'),
    ('Netherlands', 'Netherlands'),
    ('Sweden', 'Sweden'),
    ('Norway', 'Norway'),
    ('Denmark', 'Denmark'),
    ('Finland', 'Finland'),
    ('Switzerland', 'Switzerland'),
    ('Austria', 'Austria'),
    ('Belgium', 'Belgium'),
    ('Ireland', 'Ireland'),
    ('New Zealand', 'New Zealand'),
    ('Japan', 'Japan'),
    ('South Korea', 'South Korea'),
    ('China', 'China'),
    ('Singapore', 'Singapore'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('India', 'India'),
    ('Brazil', 'Brazil'),
    ('Mexico', 'Mexico'),
    ('Argentina', 'Argentina'),
    ('Chile', 'Chile'),
    ('South Africa', 'South Africa'),
    ('Russia', 'Russia'),
    ('Ukraine', 'Ukraine'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Greece', 'Greece'),
    ('Turkey', 'Turkey'),
    ('Czech Republic', 'Czech Republic'),
    ('Hungary', 'Hungary'),
    ('Malaysia', 'Malaysia'),
    ('Thailand', 'Thailand'),
    ('Indonesia', 'Indonesia'),
    ('Vietnam', 'Vietnam'),
    ('Philippines', 'Philippines'),
    ('Egypt', 'Egypt'),
    ('Israel', 'Israel'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Colombia', 'Colombia'),
    ('Peru', 'Peru'),
    ('Pakistan', 'Pakistan'),
    ('Bangladesh', 'Bangladesh'),
    ('Nigeria', 'Nigeria'),
    ('Kenya', 'Kenya'),
    ('Morocco', 'Morocco'),
    ('Qatar', 'Qatar'),
    ('Kuwait', 'Kuwait'),
    ('Oman', 'Oman'),
    ('Lebanon', 'Lebanon'),
    ('Kyrgyzstan', 'Kyrgyzstan'), 
)


class Documents(models.Model):
    document = models.FileField(upload_to='documents/')


class Cards(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')  

    country = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER, max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    name_father = models.CharField(max_length=30)
    surname_father = models.CharField(max_length=50)
    name_mother = models.CharField(max_length=30)
    surname_mother = models.CharField(max_length=50)
    siblings = models.PositiveIntegerField(default=0)

    degree = models.CharField(choices=DEGREES, max_length=15)
    previous_school = models.CharField(max_length=200)
    status_of_studies = models.CharField(max_length=15, choices=STATUS_OF_STUDIES)
    graduation = models.DateField()
    study_country = models.CharField(max_length=50)
    study_address = models.CharField(max_length=100)
    study_language = models.CharField(max_length=50)
    gpa = models.FloatField()

    wanted_degrees = models.CharField(choices=WANTED_DEGREES, max_length=200)
    wanted_countries = models.CharField(choices=WANTED_COUNTRIES, max_length=200)
    financial_support = models.BooleanField(default=False)

    essay = models.CharField(max_length=5000, null=True, blank=True)
    diploma = models.FileField(upload_to='diploma/')
    documents = models.ManyToManyField(Documents, related_name='cards')
    

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class Documents(models.Model):
    card = models.ForeignKey(Cards, on_delete=models.CASCADE, related_name='cards_document')
    document = models.FileField(upload_to='documents/')

