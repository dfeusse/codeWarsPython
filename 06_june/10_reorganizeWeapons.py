'''
The citizens of Chima need your help. Their weapons got mixed up! They need you to write a 
program that accepts the name of a character in Chima then tells which weapon he/she owns. 
For example: your program should return a solution in the format: "Gorzan-Cudjak". You must 
complete the following characters: Laval(Shado Valious), Cragger(Vengdualize), 
Lagravis(Blazeprowlor), Crominus(Grandorius), Tormak(Tygafyre), and LiElla(Roarburn). 
Return "Not a character" for invalid inputs.

>>> dic = {"dan":10,"lisap":12}
>>> dic["dan"]
'''

def weapon(name):
	characters = {"Laval":"Shado Valious", "Cragger":"Vengdualize", "Lagravis":"Blazeprowlor", "Crominus":"Grandorius", "Tormak":"Tygafyre", "LiElla":"Roarburn"}
	try:
		return name + "-" + characters[name]
	except KeyError:
		return "Not a character"
	

print weapon("G'loona")

'''
def identify_weapon(character):
    tbl = {
      "Laval"    : "Laval-Shado Valious",
      "Cragger"  : "Cragger-Vengdualize",
      "Lagravis" : "Lagravis-Blazeprowlor",
      "Crominus" : "Crominus-Grandorius",
      "Tormak"   : "Tormak-Tygafyre",
      "LiElla"   : "LiElla-Roarburn"
    }
    
    return tbl.get(character, "Not a character")

def identify_weapon(character):
    #insert your code here...FOR CHIMA!
    try:
        return character + "-" + {
        "Laval":"Shado Valious", "Cragger":"Vengdualize",
        "Lagravis":"Blazeprowlor","Crominus":"Grandorius",
        "Tormak":"Tygafyre", "LiElla":"Roarburn"
        }[character]
    except:
        return "Not a character"
'''