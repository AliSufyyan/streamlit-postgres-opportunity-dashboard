INSERT INTO opportunities
  (company_name, job_title, category, city, country, work_mode, required_skills,
   salary_min, salary_max, currency, experience_level, application_deadline, status, source_link)
VALUES
-- Data Science
('Systems Limited',    'Data Scientist',          'Data Science',       'Lahore',     'Pakistan', 'Hybrid',  'Python, Pandas, Scikit-learn', 80000, 130000, 'PKR', 'Mid',    '2026-08-01', 'Open',       'https://systemslimited.com'),
('Netsol Technologies','Junior Data Analyst',     'Data Science',       'Lahore',     'Pakistan', 'Onsite',  'SQL, Excel, Power BI',         50000,  80000, 'PKR', 'Entry',  '2026-07-15', 'Open',       'https://netsoltech.com'),
('10Pearls',           'Senior Data Engineer',    'Data Science',       'Karachi',    'Pakistan', 'Remote',  'Python, Spark, AWS',          150000, 220000, 'PKR', 'Senior', '2026-07-10', 'Open',       'https://10pearls.com'),
('Arbisoft',           'ML Engineer',             'Data Science',       'Lahore',     'Pakistan', 'Hybrid',  'TensorFlow, Python, Docker',  120000, 180000, 'PKR', 'Mid',    '2026-06-20', 'Closed',     'https://arbisoft.com'),
('Folio3',             'Data Science Intern',     'Data Science',       'Karachi',    'Pakistan', 'Remote',  'Python, Jupyter, NumPy',       30000,  50000, 'PKR', 'Entry',  '2026-07-30', 'Open',       'https://folio3.com'),

-- AI / Machine Learning
('i2c Inc',            'AI Research Engineer',    'AI',                 'Lahore',     'Pakistan', 'Onsite',  'Deep Learning, PyTorch, NLP', 180000, 250000, 'PKR', 'Senior', '2026-08-10', 'Open',       'https://i2cinc.com'),
('Confiz',             'NLP Engineer',            'AI',                 'Lahore',     'Pakistan', 'Hybrid',  'spaCy, Transformers, Python', 100000, 160000, 'PKR', 'Mid',    '2026-07-05', 'Shortlisted','https://confiz.com'),
('Tkxel',             'Computer Vision Intern',  'AI',                 'Islamabad',  'Pakistan', 'Remote',  'OpenCV, Python, CNNs',         25000,  45000, 'PKR', 'Entry',  '2026-06-25', 'Expired',    'https://tkxel.com'),
('Rapidev',            'AI Product Engineer',     'AI',                 'Lahore',     'Pakistan', 'Remote',  'Python, FastAPI, LangChain',  130000, 200000, 'PKR', 'Mid',    '2026-08-20', 'Open',       'https://rapidev.com'),
('Devsinc',            'MLOps Engineer',          'AI',                 'Islamabad',  'Pakistan', 'Hybrid',  'Docker, Kubernetes, MLflow',  140000, 210000, 'PKR', 'Mid',    '2026-07-25', 'Open',       'https://devsinc.com'),

-- Web Development
('Techlets',           'React Developer',         'Web Development',    'Karachi',    'Pakistan', 'Remote',  'React, TypeScript, REST APIs', 90000, 140000, 'PKR', 'Mid',    '2026-07-18', 'Open',       'https://techlets.io'),
('Invozone',           'Full Stack Developer',    'Web Development',    'Lahore',     'Pakistan', 'Hybrid',  'Node.js, React, MongoDB',     110000, 170000, 'PKR', 'Mid',    '2026-08-05', 'Open',       'https://invozone.com'),
('QBatch',             'Backend Developer',       'Web Development',    'Lahore',     'Pakistan', 'Onsite',  'Django, PostgreSQL, Docker',   80000, 130000, 'PKR', 'Entry',  '2026-07-12', 'Closed',     'https://qbatch.com'),
('Cubix',              'Frontend Intern',         'Web Development',    'Islamabad',  'Pakistan', 'Onsite',  'HTML, CSS, JavaScript',        20000,  40000, 'PKR', 'Entry',  '2026-06-30', 'Expired',    'https://cubix.co'),
('Contour Software',   'Senior Full Stack Dev',   'Web Development',    'Karachi',    'Pakistan', 'Remote',  'Vue.js, Python, AWS',         160000, 230000, 'PKR', 'Senior', '2026-08-15', 'Open',       'https://contour-software.com'),

-- Cyber Security
('Securiti.ai',        'Security Analyst',        'Cyber Security',     'Lahore',     'Pakistan', 'Remote',  'SIEM, Splunk, Network Security',120000,190000,'PKR', 'Mid',    '2026-07-22', 'Open',       'https://securiti.ai'),
('PTCL',               'SOC Analyst',             'Cyber Security',     'Islamabad',  'Pakistan', 'Onsite',  'IDS/IPS, Wireshark, SIEM',     80000, 120000, 'PKR', 'Entry',  '2026-07-28', 'Open',       'https://ptcl.com.pk'),
('Netsol Technologies','Cyber Security Intern',   'Cyber Security',     'Lahore',     'Pakistan', 'Hybrid',  'Linux, Python, Kali',          25000,  45000, 'PKR', 'Entry',  '2026-06-18', 'Shortlisted','https://netsoltech.com'),
('10Pearls',           'Penetration Tester',      'Cyber Security',     'Karachi',    'Pakistan', 'Remote',  'Metasploit, OWASP, Burp Suite',140000,200000,'PKR', 'Senior', '2026-08-25', 'Open',       'https://10pearls.com'),
('Systems Limited',    'Information Security Eng','Cyber Security',     'Islamabad',  'Pakistan', 'Onsite',  'ISO 27001, Risk Management',   90000, 140000, 'PKR', 'Mid',    '2026-07-20', 'Closed',     'https://systemslimited.com'),

-- Software Engineering
('Arbisoft',           'Software Engineer',       'Software Engineering','Lahore',    'Pakistan', 'Hybrid',  'Python, Django, REST',        100000, 160000, 'PKR', 'Mid',    '2026-08-08', 'Open',       'https://arbisoft.com'),
('Folio3',             'iOS Developer',           'Software Engineering','Karachi',   'Pakistan', 'Hybrid',  'Swift, Xcode, Core Data',     110000, 170000, 'PKR', 'Mid',    '2026-07-14', 'Open',       'https://folio3.com'),
('i2c Inc',            'Software Dev Intern',     'Software Engineering','Lahore',    'Pakistan', 'Onsite',  'Java, Spring Boot, Git',       30000,  55000, 'PKR', 'Entry',  '2026-06-22', 'Expired',    'https://i2cinc.com'),
('Devsinc',            'DevOps Engineer',         'Software Engineering','Islamabad', 'Pakistan', 'Remote',  'AWS, Terraform, CI/CD',       130000, 200000, 'PKR', 'Mid',    '2026-07-30', 'Open',       'https://devsinc.com'),
('Tkxel',             'Android Developer',       'Software Engineering','Lahore',    'Pakistan', 'Hybrid',  'Kotlin, Android SDK, Firebase',95000, 150000, 'PKR', 'Mid',    '2026-08-12', 'Open',       'https://tkxel.com'),

-- More records to hit 40+ total
('Rapidev',            'QA Engineer',             'Software Engineering','Karachi',   'Pakistan', 'Remote',  'Selenium, Pytest, JIRA',       70000, 110000, 'PKR', 'Entry',  '2026-07-08', 'Open',       'https://rapidev.com'),
('Confiz',             'Cloud Engineer',          'Software Engineering','Lahore',    'Pakistan', 'Hybrid',  'Azure, Docker, Kubernetes',   120000, 185000, 'PKR', 'Mid',    '2026-08-18', 'Open',       'https://confiz.com'),
('Invozone',           'Data Engineer',           'Data Science',       'Islamabad',  'Pakistan', 'Remote',  'Airflow, Spark, Python',      115000, 175000, 'PKR', 'Mid',    '2026-07-26', 'Shortlisted','https://invozone.com'),
('QBatch',             'ML Research Intern',      'AI',                 'Lahore',     'Pakistan', 'Onsite',  'Python, Research, Statistics', 20000,  40000, 'PKR', 'Entry',  '2026-07-04', 'Expired',    'https://qbatch.com'),
('Cubix',              'Game Developer',          'Software Engineering','Islamabad', 'Pakistan', 'Remote',  'Unity, C#, Game Design',       85000, 130000, 'PKR', 'Mid',    '2026-08-22', 'Open',       'https://cubix.co'),
('Contour Software',   'Business Analyst',        'Data Science',       'Karachi',    'Pakistan', 'Hybrid',  'Excel, SQL, Tableau',          75000, 110000, 'PKR', 'Entry',  '2026-07-16', 'Open',       'https://contour-software.com'),
('Securiti.ai',        'Privacy Engineer',        'Cyber Security',     'Lahore',     'Pakistan', 'Remote',  'GDPR, Python, Data Governance',140000,210000,'PKR', 'Senior', '2026-08-28', 'Open',       'https://securiti.ai'),
('PTCL',               'Network Engineer',        'Software Engineering','Islamabad', 'Pakistan', 'Onsite',  'CCNA, Routing, Firewalls',     80000, 125000, 'PKR', 'Entry',  '2026-07-24', 'Open',       'https://ptcl.com.pk'),
('Systems Limited',    'BI Developer',            'Data Science',       'Lahore',     'Pakistan', 'Hybrid',  'Power BI, SQL, SSRS',          90000, 140000, 'PKR', 'Mid',    '2026-08-02', 'Open',       'https://systemslimited.com'),
('Arbisoft',           'React Native Developer',  'Web Development',    'Islamabad',  'Pakistan', 'Remote',  'React Native, Expo, REST',    105000, 160000, 'PKR', 'Mid',    '2026-07-19', 'Closed',     'https://arbisoft.com'),
('Netsol Technologies','ERP Consultant',          'Software Engineering','Lahore',    'Pakistan', 'Onsite',  'SAP, Oracle, Business Analysis',85000,135000,'PKR', 'Mid',    '2026-08-06', 'Open',       'https://netsoltech.com'),
('10Pearls',           'UI/UX Designer',          'Web Development',    'Karachi',    'Pakistan', 'Hybrid',  'Figma, Adobe XD, CSS',         70000, 110000, 'PKR', 'Entry',  '2026-07-11', 'Open',       'https://10pearls.com'),
('Folio3',             'Blockchain Developer',    'Software Engineering','Lahore',    'Pakistan', 'Remote',  'Solidity, Ethereum, Web3.js', 150000, 230000, 'PKR', 'Senior', '2026-08-30', 'Open',       'https://folio3.com'),
('Devsinc',            'Technical Writer',        'Software Engineering','Islamabad', 'Pakistan', 'Remote',  'Markdown, API Docs, Git',      55000,  85000, 'PKR', 'Entry',  '2026-07-07', 'Open',       'https://devsinc.com'),
('i2c Inc',            'Product Manager',         'Software Engineering','Lahore',    'Pakistan', 'Hybrid',  'Agile, JIRA, Roadmapping',    130000, 200000, 'PKR', 'Senior', '2026-08-16', 'Open',       'https://i2cinc.com'),
('Invozone',           'Cyber Security Analyst',  'Cyber Security',     'Karachi',    'Pakistan', 'Onsite',  'SOC, SIEM, Threat Hunting',   100000, 155000, 'PKR', 'Mid',    '2026-07-23', 'Shortlisted','https://invozone.com');