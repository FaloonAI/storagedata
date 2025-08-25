import asyncio

# Процессы - запускают отдельные копии программ, используют несколько ядер процессора.
# Потоки - одно ядро, но много параллельных нитей.
# Асинхронность - один поток, одно ядро, но переключается между задачами только в местах await.

# Корутина = функция, объявленная с async def, которая:
   # Не выполняется сразу, а возвращает «объект-задачу» (корутину).
   # Может приостановить работу в точке await, отдав управление другим задачам.
   # Потом возобновляется с того же места.

# Event loop (цикл событий) - 
    # «Дирижёр» всех корутин. 
    # Переключает задачи в местах await.
    # Создаётся автоматически через asyncio.run().

# asyncio.gather - запускает несколько функций-корутин одновременно.
# asyncio.create_task - позволяет запускать функцию - корутину не дожидаясь ее ответа, другими словами в "фоне".

# input() блокирует event loop
# return_exceptions=True в gather - нужен для того чтобы не прерывать работу других задач из-за критической ошибки в одной.

# Python создаёт объект-корутину main().
async def main():
    print("Старт") # Выводим начало
    user_name, user_subname = await asyncio.gather(
        name(), 
        subname(),
        return_exceptions=True
    ) # это «оркестр», который берёт несколько корутин и запускает их одновременно в одном event loop.

    # Пример фоновой задачи: считаем длину имени
    task = asyncio.create_task(len_n_s(user_name))

    await asyncio.sleep(6) # ждем выполнения: ожидаем 6 секунд
    print("Объединённое имя:", user_name + " " + user_subname) # выводим

    await task

async def len_n_s(user_name):
    await asyncio.sleep(2)  # имитация работы
    print("Длина имени:", len(user_name))

async def name():
    user_name = input("Введите свое имя: ") # ввод имени
    await asyncio.sleep(5) # ждем выполнения: ожидаем 5 секунд
    print("Имя готово:", user_name) # выводим
    return user_name # возвращаем из функции

async def subname():
    user_subname = input("Введите свою фамилию: ") # вводи фамилии
    await asyncio.sleep(3) # ждем выполнения: ожидание 3 секунды
    print("Фамилия готова:", user_subname) # вывод
    return user_subname # возвращаем из функции

asyncio.run(main()) # asyncio.run запускает event loop (дирижёра).