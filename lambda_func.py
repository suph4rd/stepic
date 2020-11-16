import requests

with open('passwords.txt', 'r') as f:
    for x in f:
        x = int(x)
        req = requests.get(f'http://numbersapi.com/{x}/math?json=true')
        is_interesting = bool(req.json()['found'])
        ansver =  "Interesting" if is_interesting else "Boring"
        print(ansver)
        with open('output.txt', 'a') as f_out:
            f_out.write(ansver + "\n")


