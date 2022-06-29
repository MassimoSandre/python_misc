import json
import os

file = open('japanese_flipcard\kanji.json', encoding="utf8")
data = json.load(file)
file.close()

while True:
    os.system('cls')
    kanji = input("Inserire il kanji (niente per terminare): ")
    if kanji == '':
        break
    new_element = {
        "kanji":kanji,
        "kun":[],
        "on":[],
        "meanings":[],
        "examples":[]
    }

    while True:
        print("Letture attualmente inserite:", end="")
        for l in new_element["kun"]:
            print(" "+l, end="")
        print("")
        reading = input("Inserire la prossima lettura kun (niente per terminare): ")
        if reading == '':
            break
        new_element["kun"].append(reading)

    while True:
        print("Letture attualmente inserite:", end="")
        for l in new_element["on"]:
            print(" "+l, end="")
        print("")
        reading = input("Inserire la prossima lettura on (niente per terminare): ")
        if reading == '':
            break
        new_element["on"].append(reading)
    
    while True:
        print("Significati attualmente inseriti:", end="")
        for l in new_element["meanings"]:
            print(" "+l, end="")
        print("")
        meaning = input("Inserire il prossimo significato (niente per terminare): ")
        if meaning == '':
            break
        new_element["meanings"].append(meaning)
            
    while True:
        print("Esempi attualmente inseriti:", end="")
        for l in new_element["examples"]:
            print(" "+l["word"], end="")
        print("")
        example = input("Inserire la prossima parola di esempio (niente per terminare): ")
        if example == '':
            break
        new_element["examples"].append({"word":example, "reading":"", "meaning":""})

        new_element["examples"][-1]["reading"] = input("Inserire la lettura di "+example+": ")
        new_element["examples"][-1]["meaning"] = input("Inserire il significato di "+example+": ")

    data.append(new_element)

    file = open('japanese_flipcard\kanji.json',"w", encoding="utf8")
    json.dump(data, file,indent=4,ensure_ascii=False)
    file.close()
