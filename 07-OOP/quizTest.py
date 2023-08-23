vegetables_list = [
    {
        'question' : 'tomato?',
        'answer' : 'pomidor',
        'a' : 'pomidor',
        'b' : 'sabzi',
        'c' : 'kartoshka',
        'd' : 'piyoz'
    },
    {
        'question' : 'carrot?',
        'answer' : 'sabzi',
        'a' : 'bodring',
        'b' : 'sabzi',
        'c' : 'kartoshka',
        'd' : 'piyoz'
    },
    {
        'question' : 'potatoes?',
        'answer' : 'kartoshka',
        'a' : 'bodring',
        'b' : 'sabzi',
        'c' : 'kartoshka',
        'd' : 'piyoz'
    }
]

class EnglishQuiz:

    def __init__(self, name, list):
        self.name = name
        self.list = list
        self.right_answer_count = 0

    def start_quiz(self):
        for questn in self.list:
            print(f"{questn['question']}\n"
                  f"A) {questn['a']}\nB) {questn['b']}\n"
                  f"C) {questn['c']}\nD) {questn['d']}\n"
                  )
            try:
                result = input(">>> ").lower()
                result = questn[result]
                if result == questn['answer']:
                    self.right_answer_count += 1
            except:
                print("Iltimos variantlarni to'g'ri kiriting!!!")
    
    def stop_quiz(self):
        send_message = f"{self.name} {len(self.list)} ta testdan,"
        send_message += f"{self.right_answer_count} tasiga to'g'ri javob berdingiz!"
        print(send_message)
            

if __name__=='__main__':
    myObj = EnglishQuiz('Nurmuhammad', vegetables_list)
    myObj.start_quiz()
    myObj.stop_quiz()
