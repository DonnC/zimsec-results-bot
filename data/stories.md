## Greeting
* greet
    - utter_ask_service

## Register & Login
* greet
    - utter_ask_service
* inform_service{"service": "register"}
    - slot{"service": "register"}
    - action_register_candidate
    - slot{"requested_slot": "candidateName"}
* inform{"PERSON": "Keith Goredema", "candidateName": "keith goredema"}
    - slot{"candidateName": "keith goredema"}
    - action_register_candidate
    - slot{"candidateName": "keith goredema"}
    - slot{"requested_slot": "candidateNumber"}
* inform_center_number{"MONEY": "3018", "candidateNumber": "#3018", "number": 3018.0, "distance": 3018.0, "volume": 3018.0, "temperature": 3018.0, "time": "3018-01-01T00:00:00.000Z"}
    - slot{"candidateNumber": "#3018"}
    - action_register_candidate
    - slot{"candidateNumber": "#3018"}
    - slot{"requested_slot": "center_number"}
* inform_center_number{"CARDINAL": "020371", "center_number": "020371", "number": 20371.0, "distance": 20371.0, "volume": 20371.0, "temperature": 20371.0}
    - slot{"center_number": "020371"}
    - action_register_candidate
    - slot{"center_number": "020371"}
    - slot{"requested_slot": "candidateLevel"}
* inform_level{"candidateLevel": "advanced level"}
    - slot{"candidateLevel": "advanced level"}
    - action_register_candidate
    - slot{"candidateLevel": "advanced level"}
    - slot{"requested_slot": "candidateBirth"}
* candidate_dob{"candidateBirth": "31/01/2002", "number": 2002.0, "distance": 2002.0, "volume": 2002.0, "temperature": 2002.0, "time": "2020-01-27T01:00:00.000Z"}
    - slot{"candidateBirth": "31/01/2002"}
    - action_register_candidate
    - slot{"candidateBirth": "31/01/2002"}
    - slot{"requested_slot": "gender"}
* candidate_gender{"gender": "male"}
    - slot{"gender": "male"}
    - action_register_candidate
    - slot{"gender": "male"}
    - slot{"requested_slot": "seat"}
* inform_seat{"DATE": "June", "seat": "june", "time": "2020-06-01T00:00:00.000Z"}
    - slot{"seat": "june"}
    - action_register_candidate
    - slot{"seat": "june"}
    - slot{"requested_slot": "year"}
* inform_center_number{"DATE": "2018", "year": "2018", "number": 2018.0, "distance": 2018.0, "volume": 2018.0, "temperature": 2018.0, "time": "2018-01-01T00:00:00.000Z"}
    - slot{"year": "2018"}
    - action_register_candidate
    - slot{"year": "2018"}
    - reset_slots
* affirm
    - action_login_candidate
    - slot{"requested_slot": "username"}
    - export

## Generated Story -6399919467481132022
* greet
    - utter_ask_service
* inform_service{"service": "register"}
    - slot{"service": "register"}
    - action_register_candidate
    - slot{"requested_slot": "candidateName"}
* inform{"PERSON": "Ruth Mlambo", "candidateName": "ruth mlambo"}
    - slot{"candidateName": "ruth mlambo"}
    - action_register_candidate
    - slot{"candidateName": "ruth mlambo"}
    - slot{"requested_slot": "candidateNumber"}
* inform_center_number{"MONEY": "3028", "candidateNumber": "#3028", "number": 3028.0, "distance": 3028.0, "volume": 3028.0, "temperature": 3028.0, "time": "3028-01-01T00:00:00.000Z"}
    - slot{"candidateNumber": "#3028"}
    - action_register_candidate
    - slot{"candidateNumber": "#3028"}
    - slot{"requested_slot": "center_number"}
* inform_center_number{"ORG": "020182", "center_number": "020182", "number": 20182.0, "distance": 20182.0, "volume": 20182.0, "temperature": 20182.0}
    - slot{"center_number": "020182"}
    - action_register_candidate
    - slot{"center_number": "020182"}
    - slot{"requested_slot": "candidateLevel"}
* inform_level{"candidateLevel": "ordinary level"}
    - slot{"candidateLevel": "ordinary level"}
    - action_register_candidate
    - slot{"candidateLevel": "ordinary level"}
    - slot{"requested_slot": "candidateBirth"}
* candidate_dob{"candidateBirth": "23/05/2001", "number": 2001.0, "distance": 2001.0, "volume": 2001.0, "temperature": 2001.0, "time": "2020-01-29T17:00:00.000Z"}
    - slot{"candidateBirth": "23/05/2001"}
    - action_register_candidate
    - slot{"candidateBirth": "23/05/2001"}
    - slot{"requested_slot": "gender"}
* candidate_gender{"gender": "female"}
    - slot{"gender": "female"}
    - action_register_candidate
    - slot{"gender": "female"}
    - slot{"requested_slot": "seat"}
* inform_seat{"DATE": "june", "seat": "june", "time": "2020-06-01T00:00:00.000Z"}
    - slot{"seat": "june"}
    - action_register_candidate
    - slot{"seat": "june"}
    - slot{"requested_slot": "year"}
* inform_center_number{"DATE": "2018", "year": "2018", "number": 2018.0, "distance": 2018.0, "volume": 2018.0, "temperature": 2018.0, "time": "2018-01-01T00:00:00.000Z"}
    - slot{"year": "2018"}
    - action_register_candidate
    - slot{"year": "2018"}
    - reset_slots
* affirm
    - action_login_candidate
    - slot{"requested_slot": "username"}
* inform{"username": "zimsectakurakunyima38", "number": 38.0, "distance": 38.0, "volume": 38.0, "temperature": 38.0, "time": "2038-01-01T00:00:00.000Z"}
    - slot{"username": "zimsectakurakunyima38"}
    - action_login_candidate
    - slot{"username": "zimsectakurakunyima38"}
    - slot{"requested_slot": "password"}
* inform{"MONEY": "$Takura483Kunyima#", "password": "$takura483kunyima#", "number": 483.0, "volume": 483.0, "temperature": 483.0, "time": "0483-01-01T00:00:00.000Z", "distance": 483.0}
    - slot{"password": "$takura483kunyima#"}
    - action_login_candidate
    - slot{"password": "$takura483kunyima#"}
    - slot{"loggedIn": "1"}
    - slot{"candidate_results": "English      A\nMaths        A\nHistory      B\nPhysics      A\nChemistry    B\nAccounts     C\n\nSubjects: 6. Passes: 6"}
* affirm
    - action_send_results_file
    - reset_slots
* thank
    - utter_thank
    - export

## Register & Login
* greet
    - utter_ask_service
* inform_service{"service": "register"}
    - slot{"service": "register"}
    - action_register_candidate
    - slot{"requested_slot": "candidateName"}
* inform{"PERSON": "Keith Goredema", "candidateName": "keith goredema"}
    - slot{"candidateName": "keith goredema"}
    - action_register_candidate
    - slot{"candidateName": "keith goredema"}
    - slot{"requested_slot": "candidateNumber"}
* inform_center_number{"MONEY": "3018", "candidateNumber": "#3018", "number": 3018.0, "distance": 3018.0, "volume": 3018.0, "temperature": 3018.0, "time": "3018-01-01T00:00:00.000Z"}
    - slot{"candidateNumber": "#3018"}
    - action_register_candidate
    - slot{"candidateNumber": "#3018"}
    - slot{"requested_slot": "center_number"}
* inform_center_number{"CARDINAL": "020371", "center_number": "020371", "number": 20371.0, "distance": 20371.0, "volume": 20371.0, "temperature": 20371.0}
    - slot{"center_number": "020371"}
    - action_register_candidate
    - slot{"center_number": "020371"}
    - slot{"requested_slot": "candidateLevel"}
* inform_level{"candidateLevel": "advanced level"}
    - slot{"candidateLevel": "advanced level"}
    - action_register_candidate
    - slot{"candidateLevel": "advanced level"}
    - slot{"requested_slot": "candidateBirth"}
* candidate_dob{"candidateBirth": "31/01/2002", "number": 2002.0, "distance": 2002.0, "volume": 2002.0, "temperature": 2002.0, "time": "2020-01-27T01:00:00.000Z"}
    - slot{"candidateBirth": "31/01/2002"}
    - action_register_candidate
    - slot{"candidateBirth": "31/01/2002"}
    - slot{"requested_slot": "gender"}
* candidate_gender{"gender": "male"}
    - slot{"gender": "male"}
    - action_register_candidate
    - slot{"gender": "male"}
    - slot{"requested_slot": "seat"}
* inform_seat{"DATE": "June", "seat": "june", "time": "2020-06-01T00:00:00.000Z"}
    - slot{"seat": "june"}
    - action_register_candidate
    - slot{"seat": "june"}
    - slot{"requested_slot": "year"}
* inform_center_number{"DATE": "2018", "year": "2018", "number": 2018.0, "distance": 2018.0, "volume": 2018.0, "temperature": 2018.0, "time": "2018-01-01T00:00:00.000Z"}
    - slot{"year": "2018"}
    - action_register_candidate
    - slot{"year": "2018"}
    - reset_slots
* affirm
    - action_login_candidate
    - slot{"requested_slot": "username"}
    - export

## Generated Story LOGIN
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* deny
    - action_login_candidate
    - slot{"requested_slot": "username"}
* inform_username{"username": "zimseckundaidakuka34", "number": 34.0, "distance": 34.0, "volume": 34.0, "temperature": 34.0, "time": "2034-01-01T00:00:00.000Z"}
    - slot{"username": "zimseckundaidakuka34"}
    - action_login_candidate
    - slot{"username": "zimseckundaidakuka34"}
    - slot{"requested_slot": "password"}
* inform_username{"password": "$kundai527dakuk!", "number": 527.0, "distance": 527.0, "volume": 527.0, "temperature": 527.0, "time": "0527-01-01T00:00:00.000Z"}
    - slot{"password": "$kundai527dakuk!"}
    - action_get_candidate_results
    - export

## Login candidate
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* deny
    - action_login_candidate
    - slot{"requested_slot": "username"}
    - export

## Generated Story Forgot Password
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* affirm
    - action_handle_forget_details
    - export

## Login & see results and get results file
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* deny
    - action_login_candidate
    - slot{"requested_slot": "username"}
* affirm{"CARDINAL": "zimsecDonatusBuruka29", "username": "zimsecdonatusburuka29", "number": 29.0, "distance": 29.0, "volume": 29.0, "temperature": 29.0, "time": "2029-01-01T00:00:00.000Z"}
    - slot{"username": "zimsecdonatusburuka29"}
    - action_login_candidate
    - slot{"username": "zimsecdonatusburuka29"}
    - slot{"requested_slot": "password"}
* affirm{"ORG": "$Donatus009Buruka&", "password": "$donatus009buruka&", "number": 9.0, "distance": 9.0, "volume": 9.0, "temperature": 9.0, "time": "2020-01-26T21:00:00.000Z"}
    - slot{"password": "$donatus009buruka&"}
    - action_login_candidate
    - slot{"password": "$donatus009buruka&"}
    - slot{"loggedIn": "1"}
    - action_get_candidate_results
    - slot{"candidate_results": "English\t\t\tA\nMaths\t\t\tA\nHistory\t\t\tB\nPhysics\t\t\tA\nChemistry\t\t\tB\nAccounts\t\t\tC"}
* affirm
    - action_send_results_file
    - reset_slots
* thank
    - utter_thank
    - export

## Forgot login details
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* affirm
    - action_handle_forget_details
    - export

## Login & no results file
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* deny
    - action_login_candidate
    - slot{"requested_slot": "username"}
* affirm{"ORG": "zimsecFaraiGododo09", "username": "zimsecfaraigododo09", "number": 9.0, "distance": 9.0, "volume": 9.0, "temperature": 9.0, "time": "2020-01-26T21:00:00.000Z"}
    - slot{"username": "zimsecfaraigododo09"}
    - action_login_candidate
    - slot{"username": "zimsecfaraigododo09"}
    - slot{"requested_slot": "password"}
* affirm{"MONEY": "$Farai082Gododo#", "password": "$farai082gododo#", "number": 82.0, "distance": 82.0, "volume": 82.0, "temperature": 82.0, "time": "1982-01-01T00:00:00.000Z"}
    - slot{"password": "$farai082gododo#"}
    - action_login_candidate
    - slot{"password": "$farai082gododo#"}
    - slot{"loggedIn": "1"}
    - action_get_candidate_results
    - slot{"candidate_results": "English\t\t\tA\nMaths\t\t\tA\nHistory\t\t\tB\nPhysics\t\t\tA\nChemistry\t\t\tB\nAccounts\t\t\tC"}
* deny
    - utter_thank
* thank
    - utter_thank
* goodbye
    - utter_goodbye
    - export

## Register, No Login
* greet
    - utter_ask_service
* inform_service{"service": "register"}
    - slot{"service": "register"}
    - action_register_candidate
    - slot{"requested_slot": "candidateName"}
* inform{"PERSON": "Henry Kubikabika", "candidateName": "henry kubikabika"}
    - slot{"candidateName": "henry kubikabika"}
    - action_register_candidate
    - slot{"candidateName": "henry kubikabika"}
    - slot{"requested_slot": "candidateNumber"}
* inform_center_number{"MONEY": "3004", "candidateNumber": "#3004", "number": 3004.0, "distance": 3004.0, "volume": 3004.0, "temperature": 3004.0, "time": "3004-01-01T00:00:00.000Z"}
    - slot{"candidateNumber": "#3004"}
    - action_register_candidate
    - slot{"candidateNumber": "#3004"}
    - slot{"requested_slot": "center_number"}
* inform_center_number{"center_number": "020301", "number": 20301.0, "distance": 20301.0, "volume": 20301.0, "temperature": 20301.0}
    - slot{"center_number": "020301"}
    - action_register_candidate
    - slot{"center_number": "020301"}
    - slot{"requested_slot": "candidateLevel"}
* inform_level{"candidateLevel": "ordinary level"}
    - slot{"candidateLevel": "ordinary level"}
    - action_register_candidate
    - slot{"candidateLevel": "ordinary level"}
    - slot{"requested_slot": "candidateBirth"}
* candidate_dob{"CARDINAL": "2/5/2002", "candidateBirth": "2/5/2002", "number": 2002.0, "time": "2002-02-05T00:00:00.000Z", "distance": 2002.0, "volume": 2002.0, "temperature": 2002.0}
    - slot{"candidateBirth": "2/5/2002"}
    - action_register_candidate
    - slot{"candidateBirth": "2/5/2002"}
    - slot{"requested_slot": "gender"}
* candidate_gender{"gender": "male"}
    - slot{"gender": "male"}
    - action_register_candidate
    - slot{"gender": "male"}
    - slot{"requested_slot": "seat"}
* inform_seat{"DATE": "November", "seat": "november", "time": "2020-11-01T00:00:00.000Z"}
    - slot{"seat": "november"}
    - action_register_candidate
    - slot{"seat": "november"}
    - slot{"requested_slot": "year"}
* inform_center_number{"DATE": "2019", "year": "2019", "number": 2019.0, "distance": 2019.0, "volume": 2019.0, "temperature": 2019.0, "time": "2019-01-01T00:00:00.000Z"}
    - slot{"year": "2019"}
    - action_register_candidate
    - slot{"year": "2019"}
    - reset_slots
* deny
    - utter_thank
    - export

## Generated Story -8517741545835423008
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* deny
    - action_login_candidate
    - slot{"requested_slot": "username"}
* inform{"username": "zimsecruthsithole98", "number": 98.0, "distance": 98.0, "volume": 98.0, "temperature": 98.0, "time": "1998-01-01T00:00:00.000Z"}
    - slot{"username": "zimsecruthsithole98"}
    - action_login_candidate
    - slot{"username": "zimsecruthsithole98"}
    - slot{"requested_slot": "password"}
* inform{"ORG": "Ruth182Sithole$", "password": "$ruth182sithole$", "number": 182.0, "distance": 182.0, "volume": 182.0, "temperature": 182.0, "time": "0182-01-01T00:00:00.000Z"}
    - slot{"password": "$ruth182sithole$"}
    - action_login_candidate
    - slot{"password": "$ruth182sithole$"}
    - slot{"loggedIn": "1"}
    - action_get_candidate_results
    - slot{"candidate_results": "English\t\t\tA\nMaths\t\t\tA\nHistory\t\t\tB\nPhysics\t\t\tA\nChemistry\t\t\tB\nAccounts\t\t\tC"}
* deny
    - utter_thank
    - export

## Handle Candidate Details reset
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* affirm
    - action_handle_forget_details
    - export


## Login & get file
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* affirm
    - action_login_candidate
    - slot{"requested_slot": "username"}
* inform_username{"username": "zimsecderreckndlovu10", "number": 10.0, "distance": 10.0, "volume": 10.0, "temperature": 10.0, "time": "2020-01-26T22:00:00.000Z"}
    - slot{"username": "zimsecderreckndlovu10"}
    - action_login_candidate
    - slot{"username": "zimsecderreckndlovu10"}
    - slot{"requested_slot": "password"}
* inform{"password": "$derreck390ndlovu@", "number": 390.0, "distance": 390.0, "volume": 390.0, "temperature": 390.0, "time": "0390-01-01T00:00:00.000Z"}
    - slot{"password": "$derreck390ndlovu@"}
    - action_login_candidate
    - slot{"password": "$derreck390ndlovu@"}
    - slot{"loggedIn": "1"}
    - action_get_candidate_results
    - slot{"candidate_results": "English\t\t\tA\nMaths\t\t\tA\nHistory\t\t\tB\nPhysics\t\t\tA\nChemistry\t\t\tB\nAccounts\t\t\tC"}
* affirm
    - action_send_results_file
    - reset_slots
* thank
    - utter_thank
    - export

## Generated Story -835029019817460496
* greet
    - utter_ask_service
* inform_service{"service": "register"}
    - slot{"service": "register"}
    - action_register_candidate
    - slot{"requested_slot": "candidateName"}
* inform{"PERSON": "Catherine Kasukusa", "candidateName": "catherine kasukusa"}
    - slot{"candidateName": "catherine kasukusa"}
    - action_register_candidate
    - slot{"candidateName": "catherine kasukusa"}
    - slot{"requested_slot": "candidateNumber"}
* inform_center_number{"MONEY": "3021", "candidateNumber": "#3021", "number": 3021.0, "distance": 3021.0, "volume": 3021.0, "temperature": 3021.0, "time": "3021-01-01T00:00:00.000Z"}
    - slot{"candidateNumber": "#3021"}
    - action_register_candidate
    - slot{"candidateNumber": "#3021"}
    - slot{"requested_slot": "center_number"}
* inform_center_number{"ORG": "020172", "center_number": "020172", "number": 20172.0, "distance": 20172.0, "volume": 20172.0, "temperature": 20172.0}
    - slot{"center_number": "020172"}
    - action_register_candidate
    - slot{"center_number": "020172"}
    - slot{"requested_slot": "candidateLevel"}
* inform_level{"candidateLevel": "advanced level"}
    - slot{"candidateLevel": "advanced level"}
    - action_register_candidate
    - slot{"candidateLevel": "advanced level"}
    - slot{"requested_slot": "candidateBirth"}
* candidate_dob{"DATE": "23/9/1998", "candidateBirth": "23/9/1998", "number": 1998.0, "distance": 1998.0, "volume": 1998.0, "temperature": 1998.0, "time": "2020-01-27T21:00:00.000Z"}
    - slot{"candidateBirth": "23/9/1998"}
    - action_register_candidate
    - slot{"candidateBirth": "23/9/1998"}
    - slot{"requested_slot": "gender"}
* candidate_gender{"gender": "female"}
    - slot{"gender": "female"}
    - action_register_candidate
    - slot{"gender": "female"}
    - slot{"requested_slot": "seat"}
* inform_seat{"DATE": "november", "seat": "november", "time": "2020-11-01T00:00:00.000Z"}
    - slot{"seat": "november"}
    - action_register_candidate
    - slot{"seat": "november"}
    - slot{"requested_slot": "year"}
* inform_center_number{"DATE": "2019", "year": "2019", "number": 2019.0, "distance": 2019.0, "volume": 2019.0, "temperature": 2019.0, "time": "2019-01-01T00:00:00.000Z"}
    - slot{"year": "2019"}
    - action_register_candidate
    - slot{"year": "2019"}
    - reset_slots
* deny
    - utter_thank
* thank
    - utter_thank
    - export

## Generated Story -7853654072632193910
* greet
    - utter_ask_service
* inform_service{"service": "login"}
    - slot{"service": "login"}
    - action_prompt_forget_details
* deny
    - action_login_candidate
    - slot{"requested_slot": "username"}
* inform{"username": "zimsectawandamox21", "number": 21.0, "distance": 21.0, "volume": 21.0, "temperature": 21.0, "time": "2020-01-27T21:00:00.000Z"}
    - slot{"username": "zimsectawandamox21"}
    - action_login_candidate
    - slot{"username": "zimsectawandamox21"}
    - slot{"requested_slot": "password"}
* inform{"password": "$tawanda333mox(", "number": 333.0, "volume": 333.0, "temperature": 333.0, "time": "0333-01-01T00:00:00.000Z", "distance": 333.0}
    - slot{"password": "$tawanda333mox("}
    - action_login_candidate
    - slot{"password": "$tawanda333mox("}
    - slot{"loggedIn": "1"}
    - action_get_candidate_results
    - slot{"candidate_results": "English\t\t\tA\nMaths\t\t\tA\nHistory\t\t\tB\nPhysics\t\t\tA\nChemistry\t\t\tB\nAccounts\t\t\tC"}
* affirm
    - action_send_results_file
    - reset_slots
* thank
    - utter_thank
    - export

