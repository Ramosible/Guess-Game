from fastapi import FastAPI
import random

app = FastAPI()
'''
Guess Game

GET /guess/{num_1}
პითონი რენდომად დააგენერირებს რიცხვს 1 დან 100 ის ჩათვლით და მოთამაშემ უნდა გამოიცნოს ეს რიცხვი, მაგალითად თუ ჩაიფიქრა 20 
და მოთამაშემ გადააწოდა 18 უნდა დაუბრუნდეს ტექსტი რომ გამოსაცნობი რიცხვი უფრო მეტია, თუ 35 გადასცა მოთამაშემ ენდპოინტმა უნდა 
დაბრუნდეს რომ გამოსაცნობი ნაკლებია და როცა 20 ს გადასცემს უნდა დააბრუნოს რამდენ ცდაში გამოიცნო სწორად რიცხვი.
დამატებითი დავალება: კარგი იქნება თამაშის ხელმეორედ დაწყების ფუნქციონალი.
'''

attempt = 0
def generate_number() -> int:
    num = random.randint(1, 100)
    #print(num)
    return num

randint = generate_number()
@app.get("/guess/{num_1}")
def root(num_1: int):
    global randint
    global attempt
    attempt+=1

    if num_1 > randint:
        return {"message": f"{num_1} is greater than the random number"}
    elif num_1 < randint:
        return {"message": f"{num_1} is less than the random number"}
    else:
        rand = randint
        randint = generate_number()
        at = attempt
        attempt = 0
        return {"message": f"You guessed correctly! The random number : {rand}, attepmpts: {at}"}

