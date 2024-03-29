# goit-algo-hw-05

## Завдання 1

Додати метод delete для видалення пар ключ-значення таблиці HashTable , яка реалізована в конспекті.

## Завдання 2

Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.

## Завдання 3

Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.

## Порівняння ефективності алгоритмів пошуку підрядка

### Алгоритми та їх ефективність

- **Алгоритм Кнута-Морріса-Пратта (KMP):**
  - Продемонстрував дуже добру продуктивність, особливо на менших текстах, з часом виконання 0.02 мс для існуючого патерну та від 0.249 мс до 1.296 мс для різних текстів та патернів.
- **Алгоритм Боєра-Мура (BM):**
  - Найкраща продуктивність серед представлених алгоритмів з часом виконання від 0.021 мс до 1.016 мс.

- **Алгоритм Рабіна-Карпа (RK):**
  - Час виконання був значно вищий, особливо для більших текстів, з результатами від 0.045 мс до 3.541 мс, що робить його менш вибірково привабливим для швидкого пошуку, особливо на великих даних.

### Висновки

- Алгоритм **Боєра-Мура** рекомендується до використання для оптимізації пошуку завдяки його високій ефективності та швидкості.
  
- Алгоритм **Кнута-Морріса-Пратта** є добрим вибором для загальних цілей пошуку, особливо з меншими текстами та коли патерн існує в тексті.

- Незважаючи на вищий час виконання, алгоритм **Рабіна-Карпа** може бути корисний у специфічних сценаріях, таких як пошук декількох патернів одночасно або пошук у великих обсягах даних.
