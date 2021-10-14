#!/usr/bin/python3

# CYSA Exam Questions!



import time
import random

class QA:
  def __init__(self, question, correct_answer, false_answer):
    self.question = question
    self.ca = correct_answer
    self.otherAnsw = false_answer

q_list = [QA("""\nAfter running an nmap scan of a system, you receive scan data that indicates the following 
                three ports are open:\n
                22/TCP
                443/TCP
                1521/TCP\n
                What services commonly run on these ports?\n\n               
                1. SMTP, NetBIOS, MySQL
                2. SSH, Microsoft DS, WINS
                3. SSH, HTTPS, Oracle
                4. FTP, HTTPS, MS-SQL\n""", "SSH, HTTPS, Oracle", ["FTP, HTTPS, MS-SQL", "SMTP, NetBIOS, MySQL", "SSH, Microsoft DS, WINS"]),
QA("""\nWhich of the following tools is best suited to querying data provided by organizations like\nthe American Registry for Internet Numbers (ARIN) as part of a footprinting or reconnaissance exercise?\n
                1. nmap
                2. traceroute
                3. regmon
                4. whois\n\n""", "whois", ["regmon", "traceroute", "nmap"]),
QA("""\nWhat type of system allows attackers to believe they have succeeded with their attack, thus providing\ndefenders with information about their attack methods and tools?\n""", "A honeypot", ["A sinkhole", "A crackpot", "A darknet"]),
QA("""\nWhat cybersecurity objective could be achieved by running your organization’s web servers in redundant,\ngeographically separate datacenters?\n""", "Availability", ["Immutability", "Integrity", "Confidentiality"]),
QA("""\nWhich of the following vulnerability scanning methods will provide the most accurate detail during a scan?\n""", "Authenticated", ["Black box", "Internal view", "External view"]),
QA("""\nIn early 2017, a flaw was discovered in the Chakra JavaScript scripting engine in Microsoft’s\nEdge browser that could allow remote execution or denial of service via a specifically crafted website.\n\nThe CVSS 3.0 score for this reads CVSS:3.0/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H\nWhat is the attack vector and the impact to integrity based on this rating?\n""", "Network, High", ["Browser, High", "System, 9, 8", "None, High"]),
QA("""\nAlice is a security engineer tasked with performing vulnerability scans for her organization.\nShe encounters a false positive error in one of her scans. What should she do about this?\n
                1. Verify that it is a false positive, and then document the exception
                2. Implement a workaround
                3. Update the vulnerability scanner
                4. Use an authenticated scan, and then document the vulnerability\n""", "Verify that it is a false positive, and then document the exception", ["Implement a workaround", "Update the vulnerability scanner", "Use an authenticated scan, and then document the vulnerability"]),
QA("""\nWhich phase of the incident response process is most likely to include gathering additional 
                evidence such as information that would support legal action?
                1. Preparation
                2. Detection and Analysis
                3. Containment, Eradication, and Recovery
                4. Post-Incident Activity and Reporting""", "Containment, Eradication, and Recovery", ["Preparation", "Detection and Analysis", "Post-Incident Activity and Reporting"]),
QA("""\nWhich of the following descriptions explains an integrity loss?\n
                1. Systems were taken offline, resulting in a loss of business income.
                2. Sensitive or proprietary information was changed or delete.
                3. Protected information was accessed or exfiltrate.
                4. Sensitive personally identifiable information was accessed or exfiltrate.""", "Sensitive or proprietary information was changed or delete.", ["Protected information was accessed or exfiltrate.", "Sensitive personally identifiable information was accessed or exfiltrate", "Systems were taken offline, resulting in a loss of business income."]),
QA("""\nWhich of the following techniques is an example of active monitoring?\n
                1. Ping
                2. RMON
                3. Netflows
                4. A network tap""", "Ping", ["Netflows", "RMON", "Netflows"])]

correct_count = 0
random.shuffle(q_list)
for question_item in q_list:
  print(question_item.question)
  print("----------------------------------------------------------------------:\n")
  possible = question_item.otherAnsw + [question_item.ca]
  random.shuffle(possible)
  count = 0
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  time.sleep(5)
  print("----------------------------------------------------------------------:\nWhat is the answer?\n")
  usrAns = input()
  while not usrAns.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    usrAns = input()
  usrAns = int(usrAns)
  while not (usrAns > 0 and usrAns <= len(possible)):
    print("\nThat number doesn't correspond to any answer. Please enter the number of your answer:\n")
    usrAns = input()
  if possible[usrAns-1] == question_item.ca:
    print("Your answer was correct.")
    correct_count += 1
  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + question_item.ca)
  print("")

print("You answered " + str(correct_count) + " of " + str(len(q_list)) + " questions correctly.")
