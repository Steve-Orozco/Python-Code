#!/usr/bin/python3

# CYSA Exam Questions!

#import time 


Welcome = input("""Welcome to Cysa+ Exam Questions!\nThere will be 10 questions.\n\nPress "Y" to continue or "N" to cancel\n\nGoodluck\n\n""")
print(" ")
while Welcome == "y" or "Y":

    def Q1():
        print("""After running an nmap scan of a system, you receive scan data that indicates the following 
                three ports are open:\n
                22/TCP
                443/TCP
                1521/TCP\n
                What services commonly run on these ports?\n\n               
                1. SMTP, NetBIOS, MySQL
                2. SSH, Microsoft DS, WINS
                3. SSH, HTTPS, Oracle
                4. FTP, HTTPS, MS-SQL\n""")
AnswerQ1 = {' ' : "3"}   
Q1()

def Q2():
    print("""Which of the following tools is best suited to querying data provided by organizations like\nthe American Registry for Internet Numbers (ARIN) as part of a footprinting or reconnaissance exercise?\n
                1. nmap
                2. traceroute
                3. regmon
                4. whois\n""")
        
AnswerQ2 = {' ' : "4"}
Q2()

def Q3():
    print("""What type of system allows attackers to believe they have succeeded with their attack, thus providing\ndefenders with information about their attack methods and tools?\n
                1. A honeypot
                2. A sinkhole
                3. A crackpot
                4. A darknet\n""")
AnswerQ3 = {' ' : "1"}
Q3()

def Q4():
    print("""What cybersecurity objective could be achieved by running your organization’s web servers in redundant,\ngeographically separate datacenters?\n
                1. Confidentiality
                2. Integrity
                3. Immutability
                4. Availability\n""")
AnswerQ4 = {' ' : "4"}
Q4()
    
def Q5():
    print("""Which of the following vulnerability scanning methods will provide the most accurate detail during a scan?\n
                1. Black box
                2. Authenticated
                3. Internal view
                4. External view\n""")
AnswerQ5 = {' ' : "2"}
Q5()

def Q6():
    print("""In early 2017, a flaw was discovered in the Chakra JavaScript scripting engine in Microsoft’s\nEdge browser that could allow remote execution or denial of service via a specifically crafted website.\n\nThe CVSS 3.0 score for this reads CVSS:3.0/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H\nWhat is the attack vector and the impact to integrity based on this rating?\n
                1. System, 9, 8
                2. Browser, High
                3. Network, High
                4. None, High\n""")
AnswerQ6 = {' ' : "3"}
Q6()
    
def Q7():
    print("""Alice is a security engineer tasked with performing vulnerability scans for her organization.\nShe encounters a false positive error in one of her scans. What should she do about this?\n
                1. Verify that it is a false positive, and then document the exception
                2. Implement a workaround
                3. Update the vulnerability scanner
                4. Use an authenticated scan, and then document the vulnerability\n""")
AnswerQ7 = {' ' : "1"}
Q7()
    
def Q8():
    print("""Which phase of the incident response process is most likely to include gathering additional 
                evidence such as information that would support legal action?
                1. Preparation
                2. Detection and Analysis
                3. Containment, Eradication, and Recovery
                4. Post-Incident Activity and Reporting""")
AnswerQ8 = {' ' : "3"}
Q8()
    
def Q9 ():
    print("""Which of the following descriptions explains an integrity loss?\n
                1. Systems were taken offline, resulting in a loss of business income.
                2. Sensitive or proprietary information was changed or delete4.
                3. Protected information was accessed or exfiltrate4.
                4. Sensitive personally identifiable information was accessed or exfiltrate4.\n""")
AnswerQ9 = {' ' : "2"}
Q9()
    
def Q10():
    print("""Which of the following techniques is an example of active monitoring?\n
                1. Ping
                2. RMON
                3. Netflows
                4. A network tap\n""")
AnswerQ10 = {' ' : "1"}
Q10()
#time.sleep(3)

    List1 = list(AnswerQ1.keys())
    List2 = list(AnswerQ2.keys())
    List3 = list(AnswerQ3.keys())
    List4 = list(AnswerQ4.keys())
    List5 = list(AnswerQ5.keys())
    List6 = list(AnswerQ6.keys())
    List7 = list(AnswerQ7.keys())
    List8 = list(AnswerQ8.keys())
    List9 = list(AnswerQ9.keys())
    List10 = list(AnswerQ10.keys())

    correct = 0
    wrong = 0 
    for keyword in List1 or List2 or List3 or List4 or List5 or List6 or List7 or List8 or List9 or List10:
        display = "{}"

        print(display.format(keyword))
        userInputAnswer = input("\nEnter Answer as digit\n: ")
        print(" ")

    if userInputAnswer == (AnswerQ1[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
        
    if userInputAnswer == (AnswerQ2[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
    if userInputAnswer == (AnswerQ3[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
        
    if userInputAnswer == (AnswerQ4[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
    if userInputAnswer == (AnswerQ5[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
        
    if userInputAnswer == (AnswerQ6[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
    if userInputAnswer == (AnswerQ7[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
        
    if userInputAnswer == (AnswerQ8[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
    if userInputAnswer == (AnswerQ9[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
        
    if userInputAnswer == (AnswerQ10[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
    # final score
    displayScore = "SCORE: {} correct and {} wrong"
    print(displayScore.format(correct, wrong))
    Welcome = input("Play again? ('y' to continue) ")
print(" ")
print("Thanks for playing")