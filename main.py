import random

answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова',
            'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже',
            'Мой ответ - нет', 'Ни�аких сомнений', 'Хорошие перспективы', 
            'Лучше не расс�азывать', 'По моим данным - нет', 'Определённо да', 
            'Зна�и говорят - да', 'Сейчас нельзя предсказать', 'Перспек�ивы не очень хорошие', 
            'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
            
running_program = True

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

name = input('Как тебя зовут? ')

print(f'Привет, {name}')

while running_program == True:

    question = input('На какой вопрос ты хочешь получтиь ответ? ')
    
    print(random.choice(answers))
    
    next_question = input('Хочешь задать еще поврос? ДА НЕТ ')
    
    if next_question.upper() == 'ДА':
        running_program = True
    else:
        running_program = False
        
print('Возвращайся если возникнут вопросы!')
