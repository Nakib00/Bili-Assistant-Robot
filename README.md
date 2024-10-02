# IUB Information Dataset

## Overview

This repository contains a dataset of information related to the Independent University, Bangladesh (IUB). The dataset is available in both English and Bangla, stored in JSON format. This information is intended for researchers, students, and anyone interested in learning more about IUB.

## Dataset Structure

The dataset consists of the following fields:

- **name**: The name of the individual or department.
- **position**: The position or title of the individual (e.g., Professor, Associate Professor).
- **department**: The department or school associated with the individual.
- **email**: The email address for contacting the individual.
- **room**: The room number of the individual in the university.

### Example JSON Structure

```json
{
	"intents": [
		{
			"tag": "greeting",
			"patterns": [
				"Hi",
				"How are you",
				"Is anyone there?",
				"Hello",
				"Good day"
			],
			"responses": [
				"Hello, thanks for visiting",
				"Good to see you",
				"Hi dear, how can I help?"
			]
		},
		{
			"tag": "goodbye",
			"patterns": [
				"Bye",
				"See you later",
				"Goodbye",
				"tata"
			],
			"responses": [
				"See you later, thanks for visiting",
				"Have a nice day",
				"Bye! Come back again soon."
			]
		},
		{
			"tag": "thanks",
			"patterns": [
				"Thanks",
				"Thank you",
				"That's helpful",
				"Thanks for the help"
			],
			"responses": [
				"Happy to help!",
				"Any time!",
				"My pleasure"
			]
		},
		{
			"tag": "name",
			"patterns": [
				"What is your name?",
				"Who are you?",
				"Tell me your name"
			],
			"responses": [
				"Bili",
				" My name is Bili",
				"i'm Bili"
			]
		},
		{
			"tag": "iubnfo",
			"patterns": [
				"What is the name of our university?",
				"What is the full name of iub?",
				"Tell me the full form of iub"
			],
			"responses": [
				"Independent University, Bangladesh"
			]
		},
		{
			"tag": "library",
			"patterns": [
				"Where is the library?",
				"Where is the library situated?",
				"Tell me about the library location"
			],
			"responses": [
				"The library is on 3th floor in BC Building",
				"The library is situated in 3th floor",
				"3th floor in BC Building"
			]
		},
		{
			"tag": "lab",
			"patterns": [
				"Where is the CSE lab one?",
				"Where is the CSE lab two?",
				"Where is the CSE lab three?",
				"Where is the CSE lab GPL?",
				"Where is the computer lab situated?",
				"Tell me about the computer lab location",
				"Computer lab"
			],
			"responses": [
				"The computer lab is on 4th floor in BC Building",
				"The computer lab is situated in 4th floor in BC Building",
				"4th floor in BC Building"
			]
		},
		{
			"tag": "phylab",
			"patterns": [
				"Where is the Physics lab?",
				"Where is the physics lab situated?",
				"Tell me about the physics lab location",
				"Physics lab"
			],
			"responses": [
				"The Physics lab is on 6th floor in BC Builging",
				"The computer lab is situated in 6th floor in BC Builging",
				"6th floor in BC Builging"
			]
		},
		{
			"tag": "hours",
			"patterns": [
				"What hours are you open?",
				"What are your hours?",
				"When are you open?"
			],
			"responses": [
				"We're open every day 8.00am-9.00pm",
				"Our hours are 8.00am-9.00pm every day"
			]
		},
		{
			"tag": "departmentheadofcse",
			"patterns": [
				"Who is the department head of CSE?",
				"Who is the department head of Computer Science & Engineering Department?",
				"What is the name of the department head of CSE"
			],
			"responses": [
				"Dr. Saadia Binte Alam"
			]
		},
		{
			"tag": "saadiabintealam",
			"patterns": [
				"Who is Saadia Binte Alam?",
				"Can you please tell me details of Dr. Saadia Binte Alam?",
				"Tell me about Dr. Saadia Binte Alam from CSE",
				"Info of Saadia Binte Alam",
				"Please provide information on Dr. Saadia Binte Alam from the CSE Department"
			],
			"responses": [
				"Dr. Saadia Binte Alam is Associate Professor and Head of the Computer Science & Engineering Department (CSE). Her Room: BC 5007D, E-mail: saadiabinte@iub.edu.bd."
			]
		},
		{
			"tag": "ashrafulamin",
			"patterns": [
				"Who is Ashraful Amin?",
				"Can you please tell me details of Dr. Md Ashraful Amin?",
				"Tell me about Dr. Md Ashraful Amin from CSE",
				"Info of Md Ashraful Amin",
				"Please provide information on Dr. Md Ashraful Amin from the CSE Department"
			],
			"responses": [
				"Dr. Md Ashraful Amin is a Professor in the Computer Science & Engineering Department (CSE). His Room: BC 5001D, E-mail: aminmdashraful@iub.edu.bd."
			]
		},
		{
			"tag": "mahbuburrahman",
			"patterns": [
				"Who is Mahbubur Rahman?",
				"Can you please tell me details of Dr. Mahbubur Rahman?",
				"Tell me about Mahbubur Rahman from CSE",
				"Info of Mahbubur Rahman",
				"Please provide information on Mahbubur Rahman from the CSE Department"
			],
			"responses": [
				"Dr. A K M Mahbubur Rahman is an Associate Professor in the Computer Science & Engineering Department (CSE). His Room: C 7008, E-mail: akmmrahman@iub.edu.bd"
			]
		},
		{
			"tag": "aminahsanali",
			"patterns": [
				"Who is Amin Ahsan Ali?",
				"Can you please tell me details of Dr. Amin Ahsan Ali?",
				"Tell me about Amin Ahsan Ali from CSE",
				"Info of Amin Ahsan Ali",
				"Please provide information on Amin Ahsan Ali from the CSE Department"
			],
			"responses": [
				"Dr. Amin Ahsan Ali is an Associate Professor in the Computer Science & Engineering Department (CSE). His Room: BC 6003, E-mail: aminali@iub.edu.bd"
			]
		},
		{
			"tag": "ferdowszahid",
			"patterns": [
				"Who is Ferdows Zahid?",
				"Can you please tell me details of Dr. Ferdows Zahid?",
				"Tell me about Ferdows Zahid from CSE",
				"Info of Ferdows Zahid",
				"Please provide information on Ferdows Zahid from the CSE Department"
			],
			"responses": [
				"Dr. Ferdows Zahid is an Associate Professor in the Computer Science & Engineering Department (CSE). His Room: BC 6006, E-mail: fzahid@iub.edu.bd"
			]
		},
		{
			"tag": "ahbubulsyeed",
			"patterns": [
				"Who is Mahbubul Syeed?",
				"Can you please tell me details of Dr. Mahbubul Syeed?",
				"Tell me about Mahbubul Syeed from CSE",
				"Info of Mahbubul Syeed",
				"Please provide information on Mahbubul Syeed from the CSE Department"
			],
			"responses": [
				"Dr. M M Mahbubul Syeed is an Associate Professor in the Computer Science & Engineering Department (CSE). His Room: C 7002, E-mail: mahbubul.syeed@iub.edu.bd"
			]
		},
		{
			"tag": "mahadyhasan",
			"patterns": [
				"Who is Mahady Hasan?",
				"Can you please tell me details of Dr. Mahady Hasan?",
				"Tell me about Mahady Hasan from CSE",
				"Info of Mahady Hasan",
				"Please provide information on Mahady Hasan from the CSE Department"
			],
			"responses": [
				"Dr. Mahady Hasan is an Associate Professor in the Computer Science & Engineering Department (CSE). His Room: BC 6001, E-mail: mahady@iub.edu.bd"
			]
		},
		{
			"tag": "mohammadfaisaluddin",
			"patterns": [
				"Who is Faisal Uddin?",
				"Can you please tell me details of Dr.Faisal Uddin?",
				"Tell me about Mohammad Faisal Uddin from CSE",
				"Info of Faisal Uddin",
				"Please provide information on Faisal Uddin from the CSE Department"
			],
			"responses": [
				"Dr. Mohammad Faisal Uddin is an Associate Professor in the Computer Science & Engineering Department (CSE). His Room: BC 5001F, E-mail: faisal@iub.edu.bd"
			]
		},
		{
			"tag": "taremahmed",
			"patterns": [
				"Who is Tarem Ahmed?",
				"Can you please tell me details of Dr. Tarem Ahmed?",
				"Tell me about Tarem Ahmed from CSE",
				"Info of Tarem Ahmed",
				"Please provide information on Tarem Ahmed from the CSE Department"
			],
			"responses": [
				"Dr. Tarem Ahmed is an Associate Professor in the Computer Science & Engineering Department (CSE). His Room: C 7011, E-mail: tarem@iub.edu.bd"
			]
		},
		{
			"tag": "ashrafulislam",
			"patterns": [
				"Who is Ashraful Islam?",
				"Can you please tell me details of Dr. Ashraful Islam?",
				"Tell me about Ashraful Islam from CSE",
				"Info of Ashraful Islam",
				"Please provide information on Ashraful Islam from the CSE Department"
			],
			"responses": [
				"Dr. Ashraful Islam is an Assistant Professor in the Computer Science & Engineering Department (CSE). His Room: MK 8004, E-mail: ashraful@iub.edu.bd"
			]
		},
		{
			"tag": "asifmahmood",
			"patterns": [
				"Who is Asif Mahmood?",
				"Can you please tell me details of Dr. Asif Mahmood?",
				"Tell me about Asif Mahmood from CSE",
				"Info of Asif Mahmood",
				"Please provide information on Asif Mahmood from the CSE Department"
			],
			"responses": [
				"Dr. Asif Mahmood is an Assistant Professor in the Computer Science & Engineering Department (CSE). His Room: C 7004, E-mail: asif.mahmood@iub.edu.bd"
			]
		},
		{
			"tag": "farzanarahman",
			"patterns": [
				"Who is Farzana Rahman?",
				"Can you please tell me details of Dr. Farzana Rahman?",
				"Tell me about Farzana Rahman from CSE",
				"Info of Farzana Rahman",
				"Please provide information on Farzana Rahman from the CSE Department"
			],
			"responses": [
				"Dr. Farzana Rahman is an Assistant Professor in the Computer Science & Engineering Department (CSE). Her Room: C 7016, E-mail: farzana.rahman@iub.edu.bd"
			]
		},
		{
			"tag": "shakhawathossain",
			"patterns": [
				"Who is Shakhawat Hossain?",
				"Can you please tell me details of Dr. Shakhawat Hossain?",
				"Tell me about Shakhawat Hossain from CSE",
				"Info of Shakhawat Hossain",
				"Please provide information on Shakhawat Hossain from the CSE Department"
			],
			"responses": [
				"Dr. Md Shakhawat Hossain is an Assistant Professor in the Computer Science & Engineering Department (CSE). His Room: C 7015, E-mail: shakhawat@iub.edu.bd"
			]
		},
		{
			"tag": "tarekhabib",
			"patterns": [
				"Who is Tarek Habib?",
				"Can you please tell me details of Dr. Tarek Habib?",
				"Tell me about Tarek Habib from CSE",
				"Info of Tarek Habib",
				"Please provide information on Tarek Habib from the CSE Department"
			],
			"responses": [
				"Dr. Md Tarek Habib is an Assistant Professor in the Computer Science & Engineering Department (CSE). His Room: BC, E-mail: tarek@iub.edu.bd"
			]
		},
		{
			"tag": "zahangiralam",
			"patterns": [
				"Who is Zahangir Alam?",
				"Can you please tell me details of Dr. Zahangir Alam?",
				"Tell me about Zahangir Alam from CSE",
				"Info of Zahangir Alam",
				"Please provide information on Zahangir Alam from the CSE Department"
			],
			"responses": [
				"Dr. Md Zahangir Alam is an Assistant Professor in the Computer Science & Engineering Department (CSE). His Room: BC, E-mail: zahangir.alam@iub.edu.bd"
			]
		},
		{
			"tag": "mohammadshidujaman",
			"patterns": [
				"Who is Shidujaman?",
				"Can you please tell me details of Dr. Shidujaman?",
				"Tell me about Shidujaman from CSE",
				"Info of Shidujaman",
				"Please provide information on Shidujaman from the CSE Department"
			],
			"responses": [
				"Dr. Mohammad Shidujaman is an Assistant Professor in the Computer Science & Engineering Department (CSE). His Room: BC, E-mail: shidujaman@iub.edu.bd"
			]
		},
		{
			"tag": "razibhayatkhan",
			"patterns": [
				"Who is Razib Hayat?",
				"Can you please tell me details of Dr. Razib Hayat Khan?",
				"Tell me about Razib Hayat Khan from CSE",
				"Info of Razib Hayat Khan",
				"Please provide information on Razib Hayat Khan from the CSE Department"
			],
			"responses": [
				"Dr. Razib Hayat Khan is an Assistant Professor in the Computer Science & Engineering Department (CSE). His Room: C 7007, E-mail: rkhan@iub.edu.bd"
			]
		},
		{
			"tag": "ajmirisabrinakhan",
			"patterns": [
				"Who is Ajmiri?",
				"Can you please tell me details of Ajmiri Sabrina Khan?",
				"Tell me about Ajmiri Sabrina Khan from CSE",
				"Info of Ajmiri Khan",
				"Please provide information on Ajmiri Sabrina Khan from the CSE Department"
			],
			"responses": [
				"Ms. Ajmiri Sabrina Khan is a Lecturer A in the Computer Science & Engineering Department (CSE). Her Room: C 7003, E-mail: ajmirikhan@iub.edu.bd"
			]
		},
		{
			"tag": "bijoyrahmanarif",
			"patterns": [
				"Who is Bijoy Arif?",
				"Can you please tell me details of Bijoy Rahman Arif?",
				"Tell me about Bijoy Rahman Arif from CSE",
				"Info of Bijoy Arif",
				"Please provide information on Bijoy Rahman Arif from the CSE Department"
			],
			"responses": [
				"Mr. Bijoy Rahman Arif is a Lecturer A in the Computer Science & Engineering Department (CSE). His Room: BC 5010, E-mail: bijoyarif@iub.edu.bd"
			]
		},
		{
			"tag": "kanizfatema",
			"patterns": [
				"Who is Kaniz Fatema?",
				"Can you please tell me details of Kaniz Fatema?",
				"Tell me about Kaniz Fatema from CSE",
				"Info of Kaniz Fatema",
				"Please provide information on Kaniz Fatema from the CSE Department"
			],
			"responses": [
				"Ms. Kaniz Fatema is a Lecturer A in the Computer Science & Engineering Department (CSE). Her Room: C 7003, E-mail: kaniz.fatema@iub.edu.bd"
			]
		},
		{
			"tag": "abusayed",
			"patterns": [
				"Who is Abu Sayed?",
				"Can you please tell me details of Abu Sayed?",
				"Tell me about Abu Sayed from CSE",
				"Info of Abu Sayed",
				"Please provide information on Abu Sayed from the CSE Department"
			],
			"responses": [
				"Mr. Md Abu Sayed is a Lecturer A in the Computer Science & Engineering Department (CSE). His Room: BC 5010, E-mail: asayed@iub.edu.bd"
			]
		},
		{
			"tag": "asifbinkhaled",
			"patterns": [
				"Who is Asif Bin Khaled?",
				"Can you please tell me details of Asif Bin Khaled?",
				"Tell me about Asif Bin Khaled from CSE",
				"Info of Asif Bin Khaled",
				"Please provide information on Asif Bin Khaled from the CSE Department"
			],
			"responses": [
				"Mr. Md Asif Bin Khaled is a Lecturer A in the Computer Science & Engineering Department (CSE). His Room: BC 5010D, E-mail: mdasifbinkhaled@iub.edu.bd"
			]
		},
		{
			"tag": "fahadmonir",
			"patterns": [
				"Who is Fahad Monir?",
				"Can you please tell me details of Fahad Monir?",
				"Tell me about Fahad Monir from CSE",
				"Info of Fahad Monir",
				"Please provide information on Fahad Monir from the CSE Department"
			],
			"responses": [
				"Mr. Md Fahad Monir is a Lecturer A in the Computer Science & Engineering Department (CSE). His Room: BC 5010, E-mail: fahad.monir@iub.edu.bd"
			]
		},
		{
			"tag": "noornabi",
			"patterns": [
				"Who is Noor Nabi?",
				"Can you please tell me details of Noor Nabi?",
				"Tell me about Noor Nabi from CSE",
				"Info of Noor Nabi",
				"Please provide information on Noor Nabi from the CSE Department"
			],
			"responses": [
				"Mr. Mohammad Noor Nabi is a Lecturer A in the Computer Science & Engineering Department (CSE). His Room: BC 6005, E-mail: mnnabi@iub.edu.bd"
			]
		},
		{
			"tag": "sabrinaalam",
			"patterns": [
				"Who is Sabrina Alam?",
				"Can you please tell me details of Sabrina Alam?",
				"Tell me about Sabrina Alam from CSE",
				"Info of Sabrina Alam",
				"Please provide information on Sabrina Alam from the CSE Department"
			],
			"responses": [
				"Ms. Sabrina Alam is a Lecturer A in the Computer Science & Engineering Department (CSE). Her Room: BC 5007, E-mail: sabrina.alam@iub.edu.bd"
			]
		}
]
}
